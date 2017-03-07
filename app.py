# Joshua Ryan Cruz
# app.py



import os
import flask
import flask_socketio
from flask_socketio import join_room, leave_room
import flask_sqlalchemy
import requests
import json
import swansonbot as bot
import links

app = flask.Flask(__name__)

users_connected = {}


import models
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print 'Someone connected!'
    isConnected = 1
    socketio.emit('isConnected', {'connected':isConnected})

@socketio.on('disconnect')
def on_disconnect():
    print 'Someone disconnected!'
    
@socketio.on('new message')
def on_new_message(data):
    botRes = bot.botResponses(data['message'])
    if botRes != "":
        models.addMessage(data['roomID'],data['userID'],data['message'])
        models.addMessage(data['roomID'],bot.botID,botRes)
    else:
        wrapped = links.getWrappedMessage(data['message'])
        models.addMessage(data['roomID'],data['userID'],wrapped)
    all_messages = models.getChatMessages(1)
    # print(json.dumps(all_messages, indent=4))
    connectedList = list(users_connected.values())
    connectedCount = len(connectedList)
    socketio.emit('all messages',{'messages' : all_messages,'connected users': connectedList, 'numberOfUsers': connectedCount},broadcast=True)
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
        loggedInFrom = 'Facebook'
        response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['fb_user_token'])
        json = response.json()
        name = json['name']
        link = json['picture']['data']['url']
        
    elif data['google_user_token']:
        loggedInFrom = 'Google'
        response = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
        json = response.json()
        name = (json['given_name'] + " " + json['family_name'])
        link = json['picture']
    welcome_message = bot.botResponses(("!! say Everyone! " + name + " has finally come to the great city of Pawnee!!"))
    models.addMessage(1, bot.botID, welcome_message)
    all_messages = models.getChatMessages(1)
    if models.userExists(link):
        user = models.getUser(link)
        key = user['userID']
        join_room(key)
        print("*************************user*************",user)
        if key not in users_connected:
            users_connected[key] = user
        connectedList = list(users_connected.values())
        print("*************************connectedList*************",connectedList)
        print(len(connectedList))
        connectedCount = len(users_connected)
        socketio.emit('login success', {"isLoggedIn": 1,'loggedInFrom':loggedInFrom, 'user': user, 'messages':all_messages, 'connected_users':connectedList, 'numberOfUsers': connectedCount},broadcast=True, room=key)

    else:
        new_user = models.addUser(name,link)
        nu_ = models.getUserByID(new_user.userID)
        key = nu_['userID']
        join_room(key)
        print("*************************user*************",nu_)
        if key not in users_connected:
            users_connected[key] = nu_
        connectedList = list(users_connected.values())
        connectedCount = len(users_connected)
        socketio.emit('login success', {"isLoggedIn": 1, 'loggedInFrom':loggedInFrom,'user': nu_,'messages':all_messages,'connected_users':connectedList, 'numberOfUsers': connectedCount},broadcast=True, room=key)
        
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# **************************END LOGIN COMPLETE***************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************

# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# **************************START LOGOUT*********************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
@socketio.on('logout')
def on_logout(data):
    logoutID = data['userID']
    user = models.getUserByID(data['userID'])
    name = user['username']
    welcome_message = bot.botResponses(("!! say Everyone! " + name + " is leaving, probably going back to...Eagleton."))
    models.addMessage(1, bot.botID, welcome_message)
    if logoutID in users_connected:
        del users_connected[logoutID]
    all_messages = models.getChatMessages(1)
    connectedList = list(users_connected.values())
    socketio.emit('someone left', {'messages':all_messages, 'connected_users':connectedList}, broadcast=True)
    socketio.emit('i left', {'isLoggedIn': 0}, room=data['userID'])
    leave_room(data['userID'])
    
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# **************************END LOGOUT COMPLETE**************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************

# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# **************************START TEST_CLIENT LOGIN**********************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************

@socketio.on('test client login')
def test_client_login(data):
    room = data['userID']
    join_room(room)
    socketio.emit('added to room', {'room': room})


# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# **************************END test_client_login************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************

if __name__ == '__main__':
    socketio.run(
         app,
         port=int(os.getenv('PORT')),
         host=os.getenv('IP', '0.0.0.0'),
         debug=True)

         
# mess

