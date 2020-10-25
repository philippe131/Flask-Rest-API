from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

#Init db
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
