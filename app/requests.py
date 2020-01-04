from flask import render_template,redirect,url_for,request
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')