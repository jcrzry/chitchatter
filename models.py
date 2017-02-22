# models.py
import flask_sqlalchemy, app
from datetime import datetime
import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# app.app = app modules app variable
#app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jcrzry:anchor99@localhost/postgres'
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = flask_sqlalchemy.SQLAlchemy(app.app)
ma = Marshmallow(app.app)

class chatroom(db.Model):
    roomID = db.Column(db.Integer, primary_key = True)
    public = db.Column(db.Boolean, default = True)
    roomName = db.Column(db.String(50))
    roomMessages = db.relationship('message', backref=db.backref('chatroom',lazy='joined'),lazy='dynamic')
    
    
    def __init__(self, roomName, public):
        self.roomName = roomName
        self.public = public
    def __repr__(self):
        return "<Room: {isPublic: %r, Room Name: %r>" %(self.public, self.roomName)

class message(db.Model):
    messID = db.Column(db.Integer, primary_key = True)
    roomID = db.Column(db.Integer,db.ForeignKey('chatroom.roomID'))
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))
    text = db.Column(db.Text)
    pubTime = db.Column(db.DateTime)
    def __init__(self, roomID, userID, text, pubTime=None):
        self.text = text
        self.userID = userID
        self.roomID = roomID
        if pubTime is None:
            pubTime = datetime.utcnow()
        self.pubTime = pubTime
    
    # @property
    # def serialize(self):
    #     if self.userID is None:
    #         thisUser = "No User"
    #     else:
    #         thisUser = user.query.get(self.userID)
    #     return {'text': self.text, 
    #         'user': thisUser.serialize
    #     }
        
    def __repr__(self):
        if self.userID is None:
            thisUser = "No User"
        else:
            thisUser = user.query.get(self.userID)
        
        return "<Message: {text: %r, user: %r>" %(self.text, thisUser)
        
class user(db.Model):
    userID = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(120))
    imgLink = db.Column(db.String(300))
    userMessages = db.relationship('message', backref=db.backref('user',lazy='joined'),lazy='dynamic')
    
    def __init__(self, username, imgLink):
        self.username = username
        self.imgLink = imgLink
        
    # @property
    # def serialize(self):
    #     return {'userID': self.userID, 'link': self.imgLink}


    def __repr__(self):
        return '<User: {name: %r, imgLink:  %r>' %(self.username,self.imgLink)
    
###########################################################################################
###########################################################################################
class messageSchema(ma.ModelSchema):
    class Meta:
        model = message
        
class userSchema(ma.ModelSchema):
    class Meta:
        model = user
        
        
###########################################################################################
###########################################################################################        
def getChatMessages(roomID):
    if roomID is None:
        return "No chatroom specified"
    else:
        allMessages = chatroom.query.get(roomID).roomMessages.all()
        mess_Scheme = messageSchema()
        all_messages = []
        for i in allMessages:
            all_messages.append( mess_Scheme.dump(i).data)
        return {'all_messages' : all_messages}
        
def userExists(link):
    row = user.query.filter_by(imgLink=link).first()
    if row is None:
        return False;
    else:
        return True;
        
def getUser(link):
    return user.query.filter_by(imgLink=link).first()
    
def addMessage(roomID, userID, text, pubTime=None):
        new_message = message(roomID,userID,text,pubTime=None)
        db.session.add(new_message)
        db.session.commit()
        
def addUser(name,link):
    new_user = user(name,link)
    db.session.add(new_user)
    db.session.commit()
    return new_user
    