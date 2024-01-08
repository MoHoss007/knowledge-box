from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError, Email
import email_validator
from knowledge_box.repositories.user_repository import UserRepository
import re


# noinspection PyMethodMayBeStatic
class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    password_confirmation = PasswordField(label="Password Confirmation", validators=[EqualTo("password"), DataRequired()])
    submit = SubmitField(label="Register")

    def validate_username(self, username_to_check):
        user = UserRepository.get_user_by_name_or_email(username_to_check.data)
        if user:
            raise ValidationError("A user with the provided username already exists.")

        allowed_characters_pattern = re.compile(r"^[a-zA-Z0-9_]+$")
        if not allowed_characters_pattern.match(username_to_check.data):
            raise ValidationError("Invalid characters in username. Use only letters, numbers, and underscores.")

    def validate_email(self, email_to_check):
        user = UserRepository.get_user_by_name_or_email(email_to_check.data)
        if user:
            raise ValidationError("A user with the provided email already exists.")


class LoginForm(FlaskForm):
    username_or_email = StringField(label="Username/Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")