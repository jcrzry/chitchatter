import os
import flask
import flask_socketio
import flask_sqlalchemy

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
app.config['SQLALCHEMY_DB_URI'] = 'postgresql://jcrzry:anchor99@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app)

socketio.run(
     app,
     host=os.getenv('IP', '0.0.0.0'),
     port=int(os.getenv('PORT', 8080)),
     debug=True)