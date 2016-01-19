from my_app import app

### added from __init__.py ### was running into import error
from my_app.hello.views import hello
from flask.ext.sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
db.create_all()
app.register_blueprint(hello)
############

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	page_hits = db.Column(db.Integer, default=0)

	def __init__(self, name): #initalize new page to 0 page_hits
		self.name = name
		self.page_hits = 0

	def __repr__(self):
		return '<Page %d>' % self.name

	def visitPage(self):
		self.page_hits = self.page_hits + 1 
 

