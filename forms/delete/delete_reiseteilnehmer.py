from flask_wtf import FlaskForm
from wtforms.fields import IntegerField

class DeleteForm(FlaskForm):
    ReisendeId = IntegerField("ReisendeId")
