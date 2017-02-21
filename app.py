# Joshua Ryan Cruz
# app.py



import os
import flask
import flask_socketio
import flask_sqlalchemy
import requests
import sys 
import logging



app = flask.Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

import models
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    
@socketio.on('new message')
def on_new_message(data):
    chat = models.db.chatroom.query(chatroomID = '1')
    socketio.emit('all messages',{'messages' : all_messages})
    print('message forwarded')
    
@socketio.on('FB login complete')
def on_FB_login_complete(data):
    response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
    json = response.json();
    print(json)
    name = json['name']
    link = json['picture']['data']['url']
    if userExists(link):
        user = models.getUser(link)
        socketio.emit('fb login success', {"isLoggedIn": True, 'user': {'id': user.userID,'name':user.username,'imgLink':user.imgLink}})
    else:
        new_user = models.user(name,link)
        socketio.emit('fb login success', {"isLoggedIn": True, 'user': {'id': new_user.userID,'name': new_user.username,'imgLink': new_user.imgLink}})
    
if __name__ == '__main__':
    socketio.run(
         app,
         host=os.getenv('IP', '0.0.0.0'),
         port=int(os.getenv('PORT', 8080)),
         debug=True)