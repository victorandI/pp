from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from config import DATABASE_URI
from waitress import serve
from flask_migrate import Migrate
import pymysql
from user import user
from car import car
from order import order
from check_models import *




app = Flask(__name__)

db = SQLAlchemy()
engine = create_engine(DATABASE_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwerty1234567@localhost:3306/pp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
ma = Marshmallow(engine)
Session = sessionmaker(bind=engine)
bcrypt = Bcrypt(app)
test()
#migrate = Migrate(app, db)
app.register_blueprint(user)
app.register_blueprint(order)
app.register_blueprint(car)



'''@app.route('/')
def hello_world():
    return 'Hello World! - 28'''

app_test = app.test_client()
if __name__ == '__main__':
    app.run(debug=True)
