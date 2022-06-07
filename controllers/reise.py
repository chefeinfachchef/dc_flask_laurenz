import sqlalchemy
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from forms.add.add_reise import AddForm
from forms.delete.delete_reise import DeleteForm
from forms.edit.edit_reise import editForm
from model.models import db, Reise

reise_blueprint = Blueprint('reise_blueprint', __name__)


@reise_blueprint.route("/reise", methods=["GET", "POST"])
def reise():
    session: sqlalchemy.orm.scoping.scoped_session = db.session


    page = request.args.get('page', 1, type=int)
    reisen = session.query(Reise).order_by(Reise.ReiseId).paginate(
        page, 14, error_out=False)

    return render_template("/reise/reise.html", reisen=reisen)


@reise_blueprint.route("/reise/add", methods=["GET", "POST"])
def reise_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_reise_form = AddForm()
    if request.method == 'POST':
        if add_reise_form.validate_on_submit():
            new_reise = Reise()

            new_reise.Kosten = add_reise_form.reiseKosten.data
            new_reise.Zielort = add_reise_form.reiseZielort.data
            new_reise.Land = add_reise_form.reiseLand.data
            new_reise.Dauer = add_reise_form.reiseDauer.data
            new_reise.Hotel = add_reise_form.reiseHotel.data
            new_reise.bueroId = add_reise_form.reiseBueroId.data
            try:
                db.session.add(new_reise)
                db.session.commit()
            except:
                flash("Ein Fehler ist aufgetreten")
                add_reise_form = AddForm()
                return render_template("reise/reise_add.html", form=add_reise_form)

            return redirect("/reise")
        else:
            return render_template("reise/reise_add.html", form=add_reise_form)
    else:
        return render_template("reise/reise_add.html", form=add_reise_form)


@reise_blueprint.route("/reise/edit", methods=["GET", "POST"])
def reise_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_reise_form = editForm()

    ReiseId = request.args["ReiseId"]

    reise_to_edit = session.query(Reise).filter(
        Reise.ReiseId == ReiseId).first()

    if request.method == "POST":
        if edit_reise_form.validate_on_submit():
            ReiseId = edit_reise_form.reiseId.data
            reise_to_edit = db.session.query(Reise).filter(
                Reise.ReiseId == ReiseId).first()

            reise_to_edit.Kosten = edit_reise_form.reiseKosten.data
            reise_to_edit.Zielort = edit_reise_form.reiseZielort.data
            reise_to_edit.Land = edit_reise_form.reiseLand.data
            reise_to_edit.Dauer = edit_reise_form.reiseDauer.data
            reise_to_edit.Hotel = edit_reise_form.reiseHotel.data
            reise_to_edit.bueroId = edit_reise_form.reiseBueroId.data

            db.session.commit()
        return redirect("/reise")
    else:
        edit_reise_form.reiseId.data = reise_to_edit.ReiseId
        edit_reise_form.reiseKosten.data = reise_to_edit.Kosten
        edit_reise_form.reiseZielort.data = reise_to_edit.Zielort
        edit_reise_form.reiseLand.data = reise_to_edit.Land
        edit_reise_form.reiseDauer.data = reise_to_edit.Dauer
        edit_reise_form.reiseHotel.data = reise_to_edit.Hotel
        edit_reise_form.reiseBueroId.data = reise_to_edit.bueroId

        return render_template("reise/reise_edit.html", form=edit_reise_form)


@reise_blueprint.route("/reise/delete", methods=["POST"])
def reise_delete():
    delete_reise_form = DeleteForm()
    if delete_reise_form.validate_on_submit():

        delete_reiseId = delete_reise_form.ReiseId.data
        reise_to_delete = db.session.query(Reise).filter(
            Reise.ReiseId == delete_reiseId)
        reise_to_delete.delete()

        db.session.commit()
        flash(f"Die Reise mit der folgenden ID wurde gelöscht: {reise_to_delete}")

    return redirect("/reise")
