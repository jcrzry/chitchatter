# models.py
import flask_sqlalchemy, app
# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jcrzry:anchor99@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)
