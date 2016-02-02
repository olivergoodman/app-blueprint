from flask import Blueprint, render_template, request
from models import Page
import app


hello = Blueprint('hello', __name__)

#create new route taking JSON parameter to determine what to log in the database
#pull database branch onto master, then delete old one and replace it with new one!

@hello.route('/_get_page_title')
def get_page_title():
	page_title = request.args.get('page_title', '', type=string)
	app.updatePageDB(page_title)
	#update DB depending on what JSON received ---> http://flask.pocoo.org/docs/0.10/patterns/jquery/

@hello.route('/')
@hello.route('/index.html')
def index():
	page_title = 'Home' 
	app.updatePageDB(page_title)
	return render_template('index.html',
		title = 'Home',
		page_title = page_title)

@hello.route('/contact.html')
def contact():
	page_title = 'Contact'
	app.updatePageDB(page_title)
	return render_template('contact.html',
	title = 'Contact',
	page_title = page_title)

