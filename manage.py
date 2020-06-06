import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import APP
from models import db

database_path = os.environ['DATABASE_URL']

default_path='postgresql://postgres:1234@localhost:5432/casting'

database_path=os.getenv('DATABASE_URL', default_path)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Import database models with app context
with app.app_context():
  from models import *

migrate = Migrate(APP, db)
manager = Manager(APP)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


