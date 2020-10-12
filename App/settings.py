# -*- encoding: utf-8 -*-

def create_url(info):
    engine = info.get("engine")
    driver = info.get("driver")
    user = info.get("user")
    password = info.get("password")
    host = info.get("host")
    port = info.get("port")
    db = info.get("db")
    return "{}+{}://{}:{}@{}:{]/{]".format(engine, driver, user, password, host, port, db)


class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    info = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "123456",
        "host": "localhost",
        "port": 3306,
        "db": "flask_tpp"
    }

    SQLALCHEMY_DATABASE_URI = create_url(info)


class TestConfig(Config):
    pass


class ProductConfig(Config):
    pass


envs = {
    "develop": DevelopConfig,
    "test": TestConfig,
    "product": ProductConfig
}
