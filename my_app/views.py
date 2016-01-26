from flask import Blueprint, render_template, request
from models import Page
import app


hello = Blueprint('hello', __name__)

	
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

