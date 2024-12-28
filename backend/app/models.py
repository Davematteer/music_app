from flask_sqlalchemy import SQLAlchemy
from run import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.model):
    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(80),nullable= False,unique = True)

class Song(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(120),nullable= False)
    artist = db.Column(db.String(120),nullable= False)
