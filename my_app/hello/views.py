from flask import Blueprint, render_template, request


hello = Blueprint('hello', __name__)


def updatePageDB():
	#retrieve data from JS somehow
	title = 'home'
	current_page = Page.query.filter_by(username=title).first()
	current_page.visitPage()


@hello.route('/')
@hello.route('/index.html')
def index():
	page_title = 'Oliver Goodman' 
	print 'index was called'
	return render_template('index.html',
		title = "Home",
		page_title = page_title)

@hello.route('/contact.html')
def contact():
	page_title = 'Contact'
	return render_template('contact.html',
	title = 'Contact',
	page_title = page_title)

