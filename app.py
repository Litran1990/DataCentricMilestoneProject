# dnsython to use the new style connection string for MongoDB Atlas.
# flask-pymongo used to wire up our database to our Flask application.
# MongoDB stores its data in a JSON like format called BSON, so we imported ObjectId from the bson library
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'mange_app'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

"""Function which displays all recipes"""
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
"""Set up our IP address and our port number so that Cloud9 knows how to run and where to run our application""" 
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)