# Joshua Ryan Cruz
# app.py



import os
import flask
import flask_socketio
import flask_sqlalchemy
import requests

app = flask.Flask(__name__)
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
    name = json['name']
    link = json['picture']['data']['url']
    if not userExists(link):
        new_user = models.user(name,link)
        models.db.session.add(new_user)
        models.db.session.commit()
    socketio.emit('fb login success', 
    {"isLoggedIn": True, 'user': {'id': new_user.userID,'name':name,'imgLink':link}})
    
def userExists(link):
    userSearchResult = models.user.query.filter_by(imgLink = link).first()
    if userSearchResult is None:
        return False
    return True
    
if __name__ == '__main__':
    socketio.run(
         app,
         host=os.getenv('IP', '0.0.0.0'),
         port=int(os.getenv('PORT', 8080)),
         debug=True)