class MainConfig:
    SECRET_KEY = 'dev'
    DEBUG=True
    TESTING=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'