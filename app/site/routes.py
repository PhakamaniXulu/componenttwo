from flask import Blueprint

mod = Blueprint('site',__name__)

@mod.route('/')
@mod.route('/index')
def index():
    return "test"