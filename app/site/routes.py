from flask import Blueprint,render_template

mod = Blueprint('site',__name__)



@mod.route('/')
@mod.route('/index')
def index():
    return render_template('index.html', title='Home')

@mod.route('/financial')
def financial():
    return render_template('financial.html', title='Financial')