from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash


# db.model を継承したUserクラスを作成
class User(db.Model):
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
