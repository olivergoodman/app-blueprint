from my_app.app import create_app, setup_database
import os.path

if __name__ == '__main__':
    app = create_app()
    #from demonstrattion
    if not os.path.isfile('/tmp/test.db'):
      setup_database(app)
    app.run()
