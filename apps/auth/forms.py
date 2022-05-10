import email

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignUpForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired(message="need username"),
            Length(1, 30, message="30字以内で入力してください。"),
        ],
    )

    email = StringField(
        "email address",
        validators=[
            DataRequired(message="need email"),
            Email(message="you should input the format of email address"),
        ],
    )

    password = PasswordField(
        "password", validators=[DataRequired(message="need password")]
    )

    submit = SubmitField("register")


class LoginForm(FlaskForm):
    email = StringField(
        "email address",
        validators=[
            DataRequired(message="need email"),
            Email(message="you should input the format of email address"),
        ],
    )

    password = PasswordField(
        "password", validators=[DataRequired(message="need password")]
    )

    submit = SubmitField("login")
