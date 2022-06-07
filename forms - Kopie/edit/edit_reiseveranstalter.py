from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField, SelectField, TimeField, DecimalField
from wtforms import validators


class editForm(FlaskForm):
    bueroId = HiddenField("bueroId")
    reiseveranstalterBundesland = StringField("reiseveranstalterBundesland")
    reiseveranstalterDescription = StringField("reiseveranstalterDescription")
    reiseveranstalterTelefonnummer = StringField("reiseveranstalterTelefonnummer")
    reiseveranstalterPostleitzahl = IntegerField("reiseveranstalterPostleitzahl")
    reiseveranstalterAdresse = StringField("reiseveranstalterAdresse")
    reiseveranstalterBueroname = StringField("reiseveranstalterBueroname")
    reiseveranstalterStadt = StringField("reiseveranstalterStadt")
