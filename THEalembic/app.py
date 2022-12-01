import flask
from flask import Flask
from sqlalchemy import exc
from waitress import serve
from werkzeug.security import check_password_hash

from check_models import *

__version__ = '0.1.0'
from flask import Flask, Response
from waitress import serve

from user import user
from car import car
from booking import booking

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(car)
app.register_blueprint(booking)


@app.route("/")
def index():
    return "<span style = 'color: red'>Wrong page</span>"


@app.route("/api/v1/hello-world-28")
def HelloWorld():
    return "<h1>Hello World 28</h1>"

#curl -X GET http://localhost:5000/api/v1/user

#test()

serve(app, port='5000')

if __name__ == '__main__':
    app.run(debug=True)
    # serve(app)

# waitress-serve --port=5000 --url-scheme=http app:app