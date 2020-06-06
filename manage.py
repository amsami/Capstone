from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import APP
from models import db
from app import create_app

# Import database models with app context
#with APP.app_context():
#  from models import *

manager = Manager(create_app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


