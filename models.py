import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

#database_filename = "database.db"
#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
#database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/casting'
#DATABASE_URL = 'postgresql://postgres:1234@localhost:5432/casting'
#database_path = 'postgres://vgaidjkhnksymk:8866d2ae6408947eb238d724326b43d7f217d072461e5b9f399c997e07e9d274@ec2-52-202-146-43.compute-1.amazonaws.com:5432/d4h14pmc2hrp8f'
database_path = os.environ['DATABASE_URL']

#if not database_path:
#    database_name = ""
#    database_path = 'postgresql://postgres:1234@localhost:5432/casting'
default_path='postgresql://postgres:1234@localhost:5432/casting-sami'

#database_path = 'postgresql://postgres:1234@localhost:5432/casting-sami'

database_path=os.getenv('DATABASE_URL', default_path)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


#db_drop_and_create_all()


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(50), nullable=False)
    release_date = Column(db.String(4), nullable=False)
    
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return{
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }