from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

# we need to create an instance of the Flask class
app = Flask(__name__)

# we need to set up the database
# this is not a real database, it is just a file on our computer
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# we can make a route, a.k.a an endpoint
@app.route("/landingpage")
def index():
    return "Hello!"

# we can make another route
@app.route("/drinks")
def drinks():
    return {"drinks":["Coffee", "Tea", "Water"]}

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

# setting the env variables:
# In PS:
#  $env:FLASK_APP="application.py"
#  $env:FLASK_ENV="development"

# In Bash:
#  export FLASK_APP=application.py
#  export FLASK_ENV=development