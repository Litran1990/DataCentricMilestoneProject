# dnsython has been installed to use the new style connection string for MongoDB Atlas.
# flask-pymongo used to wire up our database to our Flask application.
# MongoDB stores its data in a JSON like format called BSON, so we imported ObjectId from the bson library
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
import bcrypt
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'mange_app'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config['SECRET_KEY'] = 'the random string'

mongo = PyMongo(app)


"""Function which displays the recipes"""
@app.route('/')
@app.route('/index')
def index():
    
    recipes = mongo.db.recipes.find().sort('recipe_name', -1).limit(6)
    
    return render_template("index.html", recipes=recipes)

#=======================================================================#    

@app.route('/register', methods=['POST', 'GET'])
def register():
    
    """User Sign Up Form"""
    
    if request.method == 'POST':
        users = mongo.db.users
        current_user = users.find_one({'username': request.form['username']})
        
        if current_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        flash('Oops, that username already exists! Please choose another one.')
            
    return render_template('register.html')

#=======================================================================#    

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    """User Login Form"""
    
    if request.method == 'POST':
        users = mongo.db.users
        logged_user = users.find_one({'username': request.form['username']})
        
        if logged_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), logged_user['password'].encode('utf-8')) == logged_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
        elif request.form['username'] != logged_user:
            flash('User Does Not Exist!')
        flash('Incorrect Password!')
    
    return render_template('login.html')

#=======================================================================#    

@app.route('/logout')
def logout():
    
    """User Logout Form""" 
    
    session.clear()
    return redirect(url_for('index'))

#=======================================================================#

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    
    """Visualize A Single Recipe"""
    
    # Here we also increment the view count by one each time an user visualizes the recipe
    view_count = mongo.db.recipes
    view_count.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'recipe_views':1}}
        )
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})     
    return render_template('view_recipe.html', recipe=the_recipe)

#=======================================================================#

@app.route('/view_recipe/<recipe_id>', methods=['POST'])
def add_comment(recipe_id):

    """Adds comments to the recipe and the user profile"""
    
    comment = { request.form['comment'] }
    
    mongo.db.recipes.find_one_and_update({"_id": ObjectId(recipe_id)}, {"$push": {'comments': comment}})
    mongo.db.users.find_one_and_update({"_id": ObjectId(user_id)}, {"$push": {'comments': comment}})
    return redirect(url_for('view_recipe'))
    
#=======================================================================#
    
if __name__ == '__main__':
    
    """Set up our IP address and our port number so that Cloud9 knows how to run and where to run our application"""
    
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)