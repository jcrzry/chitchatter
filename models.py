# models.py
import flask_sqlalchemy, app
from flask_sqlalchemy import Column

# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jcrzry:anchor99@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)

class chatroom(db.Model):
    roomID = db.Column(db.Integer, primary_key = True)
    public = db.Column(db.Boolean, default = True)
    messages = db.relationship('messages', backref='chatroom',lazy='dyanmic')
    def __init__(self, roomID, public):
        self.roomID = roomID
        self.public = public

class message(db.Model):
    messID = db.Column(db.Integer, primary_key = True)
    roomID = db.Column(db.Integer,db.ForeignKey('chatroom.roomID'))
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))
    text = db.Column(db.text)
    
    def __init__(self, userID, text):
        self.useriD = user.userID
        self.message = text
        
class user(db.Model):
    userID = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120))
    imgLink = db.Column(db.String(300))
    
    def __init__(self, username, imgLink):
        self.username = username
        self.imgLink = imgLink
        
    def __repr__(self):
        return '<Username:> %s ' %self.username, '<User_img: %s>'%self.imgLink
        

