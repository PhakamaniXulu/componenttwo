from flask import Flask

app = Flask(__name__)

from app.componenttwo.routes import mod

app.register_blueprint(componenttwo.routes.mod)