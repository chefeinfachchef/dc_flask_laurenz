from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField, SelectField, TimeField
from wtforms import validators


class AddForm(FlaskForm):
    teilnehmerVorname = StringField("teilnehmerVorname")
    teilnehmerNachname = StringField("teilnehmerNachname")
    teilnehmerAdresse = StringField("teilnehmerAdresse")
    teilnehmerBundesland = StringField("teilnehmerBundesland")
    teilnehmerTelefonnummer = StringField("teilnehmerTelefonnummer")
