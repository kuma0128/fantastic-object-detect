from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = "dagfiul3d8dSKdfpGN120fi"
    WTF_CSRF_SECRET_KEY = "Alcieml93pvU2cW29ap1COI"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
