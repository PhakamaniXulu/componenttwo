from flask import Flask

app = Flask(__name__)

from app.site.routes import mod

app.register_blueprint(site.routes.mod)