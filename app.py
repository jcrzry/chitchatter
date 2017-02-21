# Joshua Ryan Cruz
# app.py



import os
import flask
import flask_socketio
import flask_sqlalchemy
import requests

app = flask.Flask(__name__)

users_connected = []

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
    all_messages = models.getChatMessages(1)
    socketio.emit('all messages',{'messages' : all_messages},broadcast=True)
    print('message forwarded')
    
@socketio.on('fb login complete')
def on_fb_login_complete(data):
    print("inside fb login")
    print(data.json)
    response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
    json = response.json();
    print(json)
    name = json['name']
    link = json['picture']['data']['url']
    if models.userExists(link):
        user = models.getUser(link)
        socketio.emit('fb login success', {"isLoggedIn": 1, 'user': {'id': user.userID,'name':user.username,'imgLink':user.imgLink}})
    else:
        new_user = models.user(name,link)
        socketio.emit('fb login success', {"isLoggedIn": 1, 'user': {'id': new_user.userID,'name': new_user.username,'imgLink': new_user.imgLink}})
    
    
    
if __name__ == '__main__':
    socketio.run(
         app,
         port=int(os.getenv('PORT')),
         host=os.getenv('IP', '0.0.0.0'),
         debug=True)

         
# mess