from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

# sqlalchemy instance
db = SQLAlchemy()

csrf = CSRFProtect()


def create_app(config_key):
    # Flask インスタンス
    app = Flask(__name__)
    # set app's config
    app.config.from_object(config[config_key])
    # CSFR　と　appの連携
    csrf.init_app(app)
    # SQLalchemy と appの連携
    db.init_app(app)
    # migrate と　appの連携
    Migrate(app, db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    from apps.auth import views as auth_views

    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app
