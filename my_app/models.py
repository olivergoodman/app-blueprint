from database import db

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

		 
 
#check first if page already exists in table. if doesn't, add to db and set its hits to 1
#create pages and add them to the database 

# def updatePageDB(title):
# 	current_page = Page.query.filter_by(name=title).first()
# 	if !current_page: #if current_page not in table, so query didn't return anything(?)
# 		db.session.add(current_page)
# 		db.session.commit()
# 	current_page.visitPage()

