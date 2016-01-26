from flask import Blueprint, render_template, request
from models import Page


hello = Blueprint('hello', __name__)

	
@hello.route('/')
@hello.route('/index.html')
def index():
	# updatePageDB('home')
	page_title = 'Oliver Goodman' 
	return render_template('index.html',
		title = "Home",
		page_title = page_title)

@hello.route('/contact.html')
def contact():
	# updatePageDB('contact')
	page_title = 'Contact'
	return render_template('contact.html',
	title = 'Contact',
	page_title = page_title)

