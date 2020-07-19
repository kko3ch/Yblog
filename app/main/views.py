from flask import render_template
from flask_login import login_required,current_user
from .. requestquote import get_random_quote
from . import main

@main.route('/', methods = ["GET","POST"])
def index():
    '''
    function that define route to index page
    '''
    quote = get_random_quote()

    return render_template('index.html',quote = quote)

    