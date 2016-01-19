from flask import Blueprint, render_template, request
from my_app.hello.models import Page

hello = Blueprint('hello', __name__)

#check first if page already exists in table. if doesn't, add to db and set its hits to 1
#create pages and add them to the database 

def updatePageDB(title):
	current_page = Page.query.filter_by(name=title).first()
	if !current_page: #if current_page not in table, so query didn't return anything(?)
		db.session.add(current_page)
		db.session.commit()
	current_page.visitPage()
	

@hello.route('/')
@hello.route('/index.html')
def index():
	updatePageDB('home')
	page_title = 'Oliver Goodman' 
	return render_template('index.html',
		title = "Home",
		page_title = page_title)

@hello.route('/contact.html')
def contact():
	updatePageDB('contact')
	page_title = 'Contact'
	return render_template('contact.html',
	title = 'Contact',
	page_title = page_title)

