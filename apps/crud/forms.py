from ast import Pass

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, length


# make user & edit form class
class UserForm(FlaskForm):
    # username の属性ラベルとヴァリデーションの設定
    username = StringField(
        "username",
        validators=[
            DataRequired(message="need username"),
            length(max=30, message="30字以内で入力してください。"),
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

    # my validator
    def validate_username(self, username):
        if not username.data:
            raise ValidationError("need username")

    submit = SubmitField("register")
