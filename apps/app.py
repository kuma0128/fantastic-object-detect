from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# sqlalchemy instance
db = SQLAlchemy()

csrf = CSRFProtect()


def create_app():
    # Flask インスタンス
    app = Flask(__name__)
    # set app's config
    app.config.from_mapping(
        SECRET_KEY="dagfiul3d8dSKdfpGN120fi",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="Alcieml93pvU2cW29ap1COI",
    )
    # CSFR　と　appの連携
    csrf.init_app(app)
    # SQLalchemy と appの連携
    db.init_app(app)
    # migrate と　appの連携
    Migrate(app, db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
