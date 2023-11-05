from flask_wtf import FlaskForm
from wtforms import SubmitField


class ProceedForm(FlaskForm):
    submit = SubmitField(label="Proceed to Quiz")
