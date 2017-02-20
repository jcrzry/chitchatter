# models.py
import flask_sqlalchemy, app
import datetime
import os

# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = flask_sqlalchemy.SQLAlchemy(app.app)

class chatroom(db.Model):
    roomID = db.Column(db.Integer, primary_key = True)
    public = db.Column(db.Boolean, default = True)
    roomName = db.Column(db.String(50))
    messages = db.relationship('message', backref='chatroom',lazy='dynamic')
    
    def __init__(self, roomName, public):
        self.roomName = roomName
        self.public = public
    def __repr__(self):
        return "<Room: %r>" %self.public

class message(db.Model):
    messID = db.Column(db.Integer, primary_key = True)
    roomID = db.Column(db.Integer,db.ForeignKey('chatroom.roomID'))
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))
    text = db.Column(db.Text)
    pubTime = db.Column(db.DateTime)
    def __init__(self, roomID, userID, text, pubTime=None):
        self.message = text
        if pubTime is None:
            pubTime = datetime.utcnow()
        self.pubTime = pubTime
        
    def __repr__(self):
        return "<User %s, Message %s>" %(self.userID.username,self.message)
        
class user(db.Model):
    userID = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120))
    imgLink = db.Column(db.String(300))
    messages = db.relationship('message', backref='user',lazy='dynamic')
    
    def __init__(self, username, imgLink):
        self.username = username
        self.imgLink = imgLink
        
    def __repr__(self):
        return '<User %s , %s>' %(self.username,self.imgLink)
        

