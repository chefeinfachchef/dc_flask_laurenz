from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import IntegerField, SelectField, TimeField, DecimalField
from wtforms import validators


class editForm(FlaskForm):
    reiseId = HiddenField("reiseId")
    reiseKosten = DecimalField("reiseKosten")
    reiseZielort = StringField("reiseZielort")
    reiseLand = StringField("reiseLand")
    reiseDauer = TimeField("reiseDauer")
    reiseHotel = StringField("reiseHotel")
    reiseBueroId = IntegerField("reiseBueroId")