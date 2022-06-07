import sqlalchemy
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from forms.add.add_reiseveranstalter import AddForm
from forms.delete.delete_reiseveranstalter import DeleteForm
from forms.edit.edit_reiseveranstalter import editForm
from model.models import Reiseveranstalter, db

reiseveranstalter_blueprint = Blueprint('reiseveranstalter_blueprint', __name__)


@reiseveranstalter_blueprint.route("/reiseveranstalter", methods=["GET", "POST"])
def reiseveranstalter():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    reiseveranstalter = session.query(Reiseveranstalter).order_by(Reiseveranstalter.bueroId).paginate(
        page, 14, error_out=False)

    return render_template("/reiseveranstalter/reiseveranstalter.html", reiseveranstalter=reiseveranstalter)


@reiseveranstalter_blueprint.route("/reiseveranstalter/edit", methods=["GET", "POST"])
def reiseveranstalter_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_reiseveranstalter_form = editForm()

    bueroId = request.args["bueroId"]

    reiseveranstalter_to_edit = session.query(Reiseveranstalter).filter(
        Reiseveranstalter.bueroId == bueroId).first()

    if request.method == "POST":
        if edit_reiseveranstalter_form.validate_on_submit():
            bueroId = edit_reiseveranstalter_form.bueroId.data
            reise_to_edit = db.session.query(Reiseveranstalter).filter(
                Reiseveranstalter.bueroId == bueroId).first()

            reiseveranstalter_to_edit.bundesland = edit_reiseveranstalter_form.reiseveranstalterBundesland.data
            reiseveranstalter_to_edit.description = edit_reiseveranstalter_form.reiseveranstalterDescription.data
            reiseveranstalter_to_edit.telefonnummer = edit_reiseveranstalter_form.reiseveranstalterTelefonnummer.data
            reiseveranstalter_to_edit.postleitzahl = edit_reiseveranstalter_form.reiseveranstalterPostleitzahl.data
            reiseveranstalter_to_edit.Adresse = edit_reiseveranstalter_form.reiseveranstalterAdresse.data
            reiseveranstalter_to_edit.Bueroname = edit_reiseveranstalter_form.reiseveranstalterBueroname.data
            reiseveranstalter_to_edit.Stadt = edit_reiseveranstalter_form.reiseveranstalterStadt.data

            db.session.commit()
        return redirect("/reiseveranstalter")
    else:
        edit_reiseveranstalter_form.bueroId.data = reiseveranstalter_to_edit.bueroId
        edit_reiseveranstalter_form.reiseveranstalterBundesland.data = reiseveranstalter_to_edit.bundesland
        edit_reiseveranstalter_form.reiseveranstalterDescription.data = reiseveranstalter_to_edit.description
        edit_reiseveranstalter_form.reiseveranstalterTelefonnummer.data = reiseveranstalter_to_edit.telefonnummer
        edit_reiseveranstalter_form.reiseveranstalterPostleitzahl.data = reiseveranstalter_to_edit.postleitzahl
        edit_reiseveranstalter_form.reiseveranstalterAdresse.data = reiseveranstalter_to_edit.Adresse
        edit_reiseveranstalter_form.reiseveranstalterBueroname.data = reiseveranstalter_to_edit.Bueroname
        edit_reiseveranstalter_form.reiseveranstalterStadt.data = reiseveranstalter_to_edit.Stadt



        return render_template("reiseveranstalter/reiseveranstalter_edit.html", form=edit_reiseveranstalter_form)


@reiseveranstalter_blueprint.route("/reiseveranstalter/add", methods=["GET", "POST"])
def reiseveranstalter_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_reiseveranstalter_form = AddForm()
    if request.method == 'POST':
        if add_reiseveranstalter_form.validate_on_submit():
            new_reise = Reiseveranstalter()

            new_reise.bundesland = add_reiseveranstalter_form.reiseveranstalterBundesland.data
            new_reise.description = add_reiseveranstalter_form.reiseveranstalterDescription.data
            new_reise.telefonnummer = add_reiseveranstalter_form.reiseveranstalterTelefonnummer.data
            new_reise.postleitzahl = add_reiseveranstalter_form.reiseveranstalterPostleitzahl.data
            new_reise.Adresse = add_reiseveranstalter_form.reiseveranstalterAdresse.data
            new_reise.Bueroname = add_reiseveranstalter_form.reiseveranstalterBueroname.data
            new_reise.Stadt = add_reiseveranstalter_form.reiseveranstalterStadt.data
            try:
                db.session.add(new_reise)
                db.session.commit()
            except:
                flash("Ein Fehler ist aufgetreten")
                add_reiseveranstalter_form = AddForm()
                return render_template("reiseveranstalter/reiseveranstalter_add.html", form=add_reiseveranstalter_form)

            return redirect("/reiseveranstalter")
        else:
            return render_template("reiseveranstalter/reiseveranstalter_add.html", form=add_reiseveranstalter_form)
    else:
        return render_template("reiseveranstalter/reiseveranstalter_add.html", form=add_reiseveranstalter_form)

@reiseveranstalter_blueprint.route("/reiseveranstalter/delete", methods=["POST"])
def reiseveranstalter_delete():
    delete_reiseveranstalter_form = DeleteForm()
    if delete_reiseveranstalter_form.validate_on_submit():

        delete_bueroId = delete_reiseveranstalter_form.bueroId.data
        reiseveranstalter_to_delete = db.session.query(Reiseveranstalter).filter(
            Reiseveranstalter.bueroId == delete_bueroId)
        reiseveranstalter_to_delete.delete()

        db.session.commit()
        flash(f"Die Reise mit der folgenden ID wurde gelöscht: {reiseveranstalter_to_delete}")

    return redirect("/reiseveranstalter")
