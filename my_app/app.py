from database import db
from flask import Flask
from models import Page
from views import hello


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/olivergoodman/Documents/github/app-blueprint/my_app/personal.db"
    db.init_app(app)    
    app.register_blueprint(hello, url_prefix='')
    return app 

def setup_database(app):
    with app.app_context():
        db.create_all()
    home = Page()
    home.name = "Home"
    contact = Page()
    contact.name = Page()
    db.session.add(home)
    db.session.add(contact)
    db.session.commit()   

 
#check first if page already exists in table. if doesn't, add to db and set its hits to 1
#create pages and add them to the database 
def updatePageDB(title):
    current_page = Page.query.filter_by(name=title).first()
    if current_page is None:
        current_page = Page(title)
    else:
        current_page.visitPage()
    db.session.add(current_page)
    db.session.commit()


