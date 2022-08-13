class MainConfig:
    SECRET_KEY = 'dev'
    DEBUG=True
    TESTING=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\Leonardo\\Documents\\PY\\ToDoVue\\Back\\data.db'