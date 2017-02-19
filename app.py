# Joshua Ryan Cruz
# app.py
#
#
import os
import flask
import flask_socketio
import flask_sqlalchemy

all_messages = []

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
    all_messages.append(data['message'])
    socketio.emit('all messages',{'messages' : all_messages})
    print('message forwarded')
    
    
    
    
    
if __name__ == '__main__':
    socketio.run(
         app,
         host=os.getenv('IP', '0.0.0.0'),
         port=int(os.getenv('PORT', 8080)),
         debug=True)