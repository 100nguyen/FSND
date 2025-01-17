import os
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)

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
    !!NOTE you can change the database_filename variable
        to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

    # add two demo rows to each table

    movie_1 = Movie(
        title='Hunt for The Red Tsunami',
        release_date='11/08/2022'
    )

    movie_1.insert()

    movie2 = Movie(
        title='Stack Is Half Full',
        release_date='11/11/2011'
    )

    movie2.insert()

    actor_1 = Actor(
        name='Helen Heroku',
        age=21,
        gender='Female'
    )

    actor_1.insert()

    actor_2 = Actor(
        name='Sammy Sudoku',
        age=26,
        gender='Male'
    )

    actor_2.insert()


'''
Movie
a persistent movie entity, extends the base SQLAlchemy Model
'''


class Movie(db.Model):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    release_date = Column(String(20), nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }


'''
Actor
a persistent actor entity, extends the base SQLAlchemy Model
'''


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }
