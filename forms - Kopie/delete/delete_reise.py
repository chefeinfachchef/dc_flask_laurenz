from flask_wtf import FlaskForm
from wtforms.fields import IntegerField

class DeleteForm(FlaskForm):
    ReiseId = IntegerField("ReiseId")
