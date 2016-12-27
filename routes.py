"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, template, redirect

from datetime import datetime

import utilities
import markovGen
import vote

URL_PREFIX = '/pastiche'

@route('/', subdomain='pastiche')
@route('/home', subdomain='pastiche')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        poets=utilities.get_poets()
    )


@route('/', subdomain='pastiche', method='POST')
def getUserChoice():
    user_selection = utilities.parse_data(request.body.read())
    result = markovGen.write(user_selection)
    global POEM
    try:
        POEM = result['poem']
    except:
        POEM = 'Sorry, please try again!'

    return redirect('/poem/' + result['id'])

@route('/poems', subdomain='pastiche')
@view('poems')
def display_poems():
    return dict(
        poems=utilities.get_poems(),
        year=datetime.now().year
    )

@route('/poem/<id>', subdomain='pastiche')
@view('poem')
def poem(id):
    return dict(
        poem=POEM,
        year=datetime.now().year
    )
    
@route('/contact', subdomain='pastiche')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Say hello!',
        year=datetime.now().year
    )

@route('/about', subdomain='pastiche')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='You are a genius.',
        year=datetime.now().year
    )

@route('/vote/<id>/<vote_dir>', subdomain='pastiche', method='PUT')
def vote_handler(id, vote_dir):
    v = vote.Vote(id, vote_dir)
    v.increment_vote()
    likes = v.return_likes()
    print likes[0]
    v.close_conn()
    return str(likes[0])
 
