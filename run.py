from my_app.app import create_app, setup_database
import os.path

if __name__ == '__main__':
    app = create_app()
    #if database doesn't exist, set it up
    if not os.path.isfile('/Users/olivergoodman/Documents/github/app-blueprint/my_app/personal.db'):
      setup_database(app)
    app.run()
