from flask import Blueprint, render_template, request, json
from models import Page
import app


hello = Blueprint('hello', __name__)

@hello.route('/_get_page_title', methods = ['GET', 'POST'])
def get_page_title():
	if request.method == 'POST':
		page_title = request.args.get('data') #work on transferring data correctly from AJAX -- 500 error
		app.updatePageDB(page_title['page_title'])

	#send back error msg/status to client side --> see AJAX tutorial
	#update DB depending on what JSON received ---> http://flask.pocoo.org/docs/0.10/patterns/jquery/

@hello.route('/')
@hello.route('/index.html')
def index():
	page_title = 'Home' 
	#app.updatePageDB(page_title)
	return render_template('index.html',
		title = 'Home',
		page_title = page_title)

@hello.route('/contact.html')
def contact():
	page_title = 'Contact'
	#app.updatePageDB(page_title)
	return render_template('contact.html',
	title = 'Contact',
	page_title = page_title)

