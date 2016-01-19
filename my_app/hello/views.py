from flask import Blueprint, render_template, request
from my_app.hello.models import MESSAGES

hello = Blueprint('hello', __name__)

@hello.route('/')
@hello.route('/index')
def index():
	page_title = 'Oliver Goodman' 
	print 'index was called'
	return render_template('index.html',
		title = "Home",
		page_title = page_title)

@hello.route('/contact')
def contact():
	page_title = 'Contact'
	return render_template('contact.html',
	title = 'Contact',
	page_title = page_title)

@hello.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key

@hello.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key 