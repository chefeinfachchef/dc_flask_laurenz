from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField, SelectField, TimeField
from wtforms import validators


class AddForm(FlaskForm):
    reiseKosten = DecimalField("reiseKosten")
    reiseZielort = StringField("reiseZielort")
    reiseLand = StringField("reiseLand")
    reiseDauer = TimeField("reiseDauer")
    reiseHotel = StringField("reiseHotel")
    reiseBueroId = DecimalField("reiseBueroId")
