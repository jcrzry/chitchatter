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
    print("********************************************",data['userID'])
    print("********************************************",data['message'])
    models.addMessage(data['roomID'],data['userID'],data['message'])
    all_messages = models.getChatMessages(1)
    # print('connected users:', users_connected)
    socketio.emit('all messages',{'messages' : all_messages,'connected users': users_connected},broadcast=True)
    print('message forwarded')


# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ****************************LOGIN COMPLETE*****************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
@socketio.on('login complete')
def on_login_complete(data):
    # print("inside fb login")
    if data['fb_user_token']:
        loggedInFrom = 'fb'
        response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
        json = response.json()
        name = json['name']
        link = json['picture']['data']['url']
        
    elif data['google_user_token']:
        loggedInFrom = 'google'
        response = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
        json = response.json()
        name = (json['given_name'] + " " + json['family_name'])
        link = json['picture']
    all_messages = models.getChatMessages(1)
    # print(all_messages)
    if models.userExists(link):
        user = models.getUser(link)
        if user not in users_connected:
            users_connected.append(user)
        socketio.emit('login success', {"isLoggedIn": 1,'loggedInFrom':loggedInFrom, 'user': user, 'messages':all_messages, 'connected_users':users_connected})
    else:
        new_user = models.addUser(name,link)
        nu_ = models.getUserByID(new_user.userID)
        if new_user not in users_connected:
            users_connected.append(nu_)
        socketio.emit('login success', {"isLoggedIn": 1, 'loggedInFrom':loggedInFrom,'user': nu_,'messages':all_messages,'connected_users':users_connected})
        
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# **************************END LOGIN COMPLETE***************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************

if __name__ == '__main__':
    socketio.run(
         app,
         port=int(os.getenv('PORT',8080)),
         host=os.getenv('IP', '0.0.0.0'),
         debug=True)

         
# mess

