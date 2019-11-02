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

mongo = PyMongo(app)


"""Function which displays the recipes"""
@app.route('/')
@app.route('/index')
def index():
    
    recipes = mongo.db.recipes.find().sort('recipe_name', -1)
    
    cards = mongo.db.recipes.find().sort('recipe_likes', 1)
    
    return render_template("index.html", recipes=recipes, cards=cards)

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
            flash('Incorrect Username')
        flash('Incorrect Password')
    
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

@app.route('/add_comment/<recipe_id>', methods=['POST'])
def add_comment(recipe_id):

    """Adds comments to the recipe and the user profile"""
    
    comment = request.form['comment']
    user = session['username']
    
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$push': {'recipe_comments': comment}})
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$push': {'recipe_users': user}})
    return redirect(url_for('view_recipe', recipe_id=recipe_id))
    
#=======================================================================#

@app.route('/add_like/<recipe_id>')
def add_like(recipe_id):
    
    """Add a like to the recipe"""
    
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'recipe_likes': 1}})
    return redirect(url_for('view_recipe', recipe_id=recipe_id))
    
#=======================================================================#

@app.route('/add_dislike/<recipe_id>')
def add_dislike(recipe_id):
    
    """Add a dislike to the recipe"""
    
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'recipe_dislikes': 1}})
    return redirect(url_for('view_recipe', recipe_id=recipe_id))
    
#=======================================================================#

@app.route('/add_recipe')
def add_recipe():
    
    """Add/Create a recipe"""
    
    return render_template('add_recipe.html', 
                            origins=mongo.db.origins.find(),
                            time=mongo.db.time.find(),
                            serving=mongo.db.serving.find(),
                            difficulty=mongo.db.difficulty.find()
                            )
    
#=======================================================================#

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    
    """Submit the new recipe to the database"""
    
    recipes = mongo.db.recipes
    
    recipes.insert_one({
        'recipe_name':request.form['recipe_name'],
        'recipe_origin':request.form['recipe_origin'],
        'recipe_time':request.form['recipe_time'],
        'recipe_serving':request.form['recipe_serving'],
        'recipe_difficulty':request.form['recipe_difficulty'],
        'recipe_image':request.form['recipe_image'],
        'recipe_ingredients':request.form['recipe_ingredients'],
        'recipe_preparation':request.form['recipe_preparation'],
        'recipe_description': request.form['recipe_description'],
        'recipe_views': 0,
        'recipe_likes': 0,
        'recipe_dislikes': 0,
        'recipe_creator':session['username']
    })
    return redirect(url_for('index'))
    
#=======================================================================#

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    
    """Edit a recipe"""
    
    the_recipe=mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    
    return render_template('edit_recipe.html',
                            recipe=the_recipe,  
                            origins=mongo.db.origins.find(),
                            time=mongo.db.time.find(),
                            serving=mongo.db.serving.find(),
                            difficulty=mongo.db.difficulty.find()
                            )
                            
#=======================================================================#

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    
    """Update the recipe to the database"""
    
    recipes = mongo.db.recipes
    
    recipes.update({'_id':ObjectId(recipe_id)},
        {"$set":{
        'recipe_name':request.form.get('recipe_name'),
        'recipe_origin':request.form.get('recipe_origin'),
        'recipe_time':request.form.get('recipe_time'),
        'recipe_serving':request.form.get('recipe_serving'),
        'recipe_difficulty':request.form.get('recipe_difficulty'),
        'recipe_image':request.form.get('recipe_image'),
        'recipe_ingredients':request.form.get('recipe_ingredients'),
        'recipe_preparation': request.form.get('recipe_preparation'),
        'recipe_description':request.form.get('recipe_description'),
        'recipe_creator':session['username']
    }})
    return redirect(url_for('index'))
    
#=======================================================================#

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    
    """Delete the recipe from the database"""
    
    recipes = mongo.db.recipes
    
    recipes.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('index'))
    
#=======================================================================#

@app.route("/filter_recipe", methods=["GET", "POST"])
def filter_recipe():
    """
    Filter by difficulty level, origin, time, and serving
    """
    
    recipes = mongo.db.recipes # Set our collection
    criteria = [] # An array for use in the mongo query
    
    if request.method == "POST":
        origins = request.form.get('recipe_origin')
        if origins is not None:
            dict1 = {
                    'recipe_origin': origins
                    }
            criteria.append(dict1)
    
        time = request.form.get('recipe_time')
        if time is not None:
            dict2 = {
                    'recipe_time': time
                    }
            criteria.append(dict2)
    
        difficulty = request.form.get('recipe_difficulty')
        if difficulty is not None:
            dict3 = {
                    'recipe_difficulty': difficulty
                }
            criteria.append(dict3)
            
        serving = request.form.get('recipe_serving')
        if serving is not None:
            dict4 = {
                    'recipe_serving' : serving
                }
            criteria.append(dict4)
        
        results = recipes.find({'$and': criteria })

        return render_template("filter_recipe.html", 
                            origins=mongo.db.origins.find(),
                            difficulty=mongo.db.difficulty.find(), 
                            results=results)
        
        print(criteria)
    
    return render_template("filter_recipe.html",
                        origins=mongo.db.origins.find(),
                        difficulty=mongo.db.difficulty.find())
    
#=======================================================================#
    
if __name__ == '__main__':
    
    """Set up our IP address and our port number so that Cloud9 knows how to run and where to run our application"""
    
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)

