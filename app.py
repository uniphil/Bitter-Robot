import os
import logging
from flask import Flask
from flask_heroku import Heroku
from pymongo import MongoClient

app = Flask(__name__)
heroku = Heroku(app)

def mongo_connection():
    try:
        host = app.config['MONGODB_HOST']
        port = app.config['MONGODB_PORT']
    except KeyError:
        logging.warning('No environment variables for mongohq found.')
        host, port = None, None
    connection = MongoClient(host=host, port=port)
    return connection

@app.route('/')
def hello():
    db = mongo_connection().test_db
    test_things = db.test_things
    test_thing = {'name': 'Robot', 'occupation': 'Being Grumpy'}
    i = test_things.insert(test_thing)
    return 'you are not my friend'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

