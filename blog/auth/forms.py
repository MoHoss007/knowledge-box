from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from blog.models import User


# noinspection PyMethodMayBeStatic
class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label="Password Confirmation", validators=[EqualTo("password"), DataRequired()])
    submit = SubmitField(label="Register")

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("A user with the provided username already exists.")

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("A user with the provided email already exists.")
