import sqlalchemy
from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from forms.add.add_reiseteilnehmer import AddForm
from forms.delete.delete_reiseteilnehmer import DeleteForm
from forms.edit.edit_reiseteilnehmer import editForm
from model.models import db, Reiseteilnehmer

reiseteilnehmer_blueprint = Blueprint('reiseteilnehmer_blueprint', __name__)


@reiseteilnehmer_blueprint.route("/reiseteilnehmer", methods=["GET", "POST"])
def reiseteilnehmer():
    session: sqlalchemy.orm.scoping.scoped_session = db.session


    page = request.args.get('page', 1, type=int)
    reiseteilnehmer = session.query(Reiseteilnehmer).order_by(Reiseteilnehmer.ReisendeId).paginate(
        page, 14, error_out=False)

    return render_template("/reiseteilnehmer/reiseteilnehmer.html", reiseteilnehmer=reiseteilnehmer)


@reiseteilnehmer_blueprint.route("/reiseteilnehmer/add", methods=["GET", "POST"])
def reiseteilnehmer_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_reiseteilnehmer_form = AddForm()
    if request.method == 'POST':
        if add_reiseteilnehmer_form.validate_on_submit():
            new_reise = Reiseteilnehmer()

            new_reise.Vorname = add_reiseteilnehmer_form.teilnehmerVorname.data
            new_reise.Nachname = add_reiseteilnehmer_form.teilnehmerNachname.data
            new_reise.Adresse = add_reiseteilnehmer_form.teilnehmerAdresse.data
            new_reise.Bundesland = add_reiseteilnehmer_form.teilnehmerBundesland.data
            new_reise.Telefonnummer = add_reiseteilnehmer_form.teilnehmerTelefonnummer.data

            try:
                db.session.add(new_reise)
                db.session.commit()
            except:
                flash("Ein Fehler ist aufgetreten")
                add_reiseteilnehmer_form = AddForm()
                return render_template("reiseteilnehmer/reiseteilnehmer_add.html", form=add_reiseteilnehmer_form)

            return redirect("/reiseteilnehmer")
        else:
            return render_template("reiseteilnehmer/reiseteilnehmer_add.html", form=add_reiseteilnehmer_form)
    else:
        return render_template("reiseteilnehmer/reiseteilnehmer_add.html", form=add_reiseteilnehmer_form)


@reiseteilnehmer_blueprint.route("/reiseteilnehmer/edit", methods=["GET", "POST"])
def reiseteilnehmer_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_reiseteilnehmer_form = editForm()

    ReisendeId = request.args["ReisendeId"]
    reiseteilnehmer_to_edit = session.query(Reiseteilnehmer).filter(
        Reiseteilnehmer.ReisendeId == ReisendeId).first()

    if request.method == "POST":
        if edit_reiseteilnehmer_form.validate_on_submit():
            ReisendeId = edit_reiseteilnehmer_form.reisendeId.data
            reise_to_edit = db.session.query(Reiseteilnehmer).filter(
                Reiseteilnehmer.ReisendeId == ReisendeId).first()

            reiseteilnehmer_to_edit.Vorname = edit_reiseteilnehmer_form.reisendeVorname.data
            reiseteilnehmer_to_edit.Nachname = edit_reiseteilnehmer_form.reisendeNachname.data
            reiseteilnehmer_to_edit.Adresse = edit_reiseteilnehmer_form.reisendeAdresse.data
            reiseteilnehmer_to_edit.Bundesland = edit_reiseteilnehmer_form.reisendeBundesland.data
            reiseteilnehmer_to_edit.Telefonnummer = edit_reiseteilnehmer_form.reisendeTelefonnummer.data

            db.session.commit()
        return redirect("/reiseteilnehmer")
    else:
        edit_reiseteilnehmer_form.reisendeId.data = reiseteilnehmer_to_edit.ReisendeId
        edit_reiseteilnehmer_form.reisendeVorname.data = reiseteilnehmer_to_edit.Vorname
        edit_reiseteilnehmer_form.reisendeNachname.data = reiseteilnehmer_to_edit.Nachname
        edit_reiseteilnehmer_form.reisendeAdresse.data = reiseteilnehmer_to_edit.Adresse
        edit_reiseteilnehmer_form.reisendeBundesland.data = reiseteilnehmer_to_edit.Bundesland
        edit_reiseteilnehmer_form.reisendeTelefonnummer.data = reiseteilnehmer_to_edit.Telefonnummer

        return render_template("reiseteilnehmer/reiseteilnehmer_edit.html", form=edit_reiseteilnehmer_form)


@reiseteilnehmer_blueprint.route("/reiseteilnehmer/delete", methods=["POST"])
def reiseteilnehmer_delete():
    delete_reiseteilnehmer_form = DeleteForm()
    if delete_reiseteilnehmer_form.validate_on_submit():
        delete_reiseId = delete_reiseteilnehmer_form.ReisendeId.data
        reiseteilnehmer_to_delete = db.session.query(Reiseteilnehmer).filter(
            Reiseteilnehmer.ReisendeId == delete_reiseId)
        reiseteilnehmer_to_delete.delete()

        db.session.commit()
        flash(f"Die Reise mit der folgenden ID wurde gelöscht: {reiseteilnehmer_to_delete}")

    return redirect("/reiseteilnehmer")