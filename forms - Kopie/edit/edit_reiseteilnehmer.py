from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField, SelectField, TimeField, DecimalField, TelField
from wtforms import validators


class editForm(FlaskForm):
    reisendeId = HiddenField("reisendeId")
    reisendeVorname = StringField("reisendeVorname")
    reisendeNachname = StringField("reisendeNachname")
    reisendeAdresse = StringField("reisendeAdresse")
    reisendeBundesland = StringField("reisendeBundesland")
    reisendeTelefonnummer = StringField("reisendeTelefonnummer")
