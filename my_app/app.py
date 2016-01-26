from database import db
from flask import Flask
from models import Page
from views import hello


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    db.init_app(app)    
    app.register_blueprint(hello, url_prefix='')
    return app 

#create function to increment database by 1, call in views.py   
def visit_page():
    return

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


