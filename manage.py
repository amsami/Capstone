from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import APP
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/casting-sami'
db = SQLAlchemy(app)
migrate = Migrate(APP, db)
manager = Manager(APP)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


