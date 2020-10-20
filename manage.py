# -*- encoding: utf-8 -*-
import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get("FLASK_ENV", "develop")
app = create_app(env)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    # from wsgiref.simple_server import make_server
    #
    # httpd = make_server("0.0.0.0", 8008, app)
    # httpd.serve_forever()
    manager.run()
