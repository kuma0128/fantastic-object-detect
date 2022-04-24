from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy instance
db = SQLAlchemy()


def create_app():
    # Flask インスタンス
    app = Flask(__name__)
    # set app's config
    app.config.from_mapping(
        SECRET_KEY="dagfiul3d8dSKdfpGN120fi",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    # SQLalchemy と appの連携
    db.init_app(app)
    # migrate と　appの連携
    Migrate(app, db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
