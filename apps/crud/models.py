from datetime import datetime

from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


# db.model を継承したUserクラスを作成
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hush = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # property for setting password
    @property
    def password(self):
        raise AttributeError("読み取り不可")

    # hash関数
    @password.setter
    def password(self, password):
        self.password_hush = generate_password_hash(password)

    # password check
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # メアドの重複チェック
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
