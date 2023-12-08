from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi


ca = certifi.where()
app = Flask(__name__)
uri = "mongodb+srv://meganclapinski:SUkH8z1RvqKcFJep@cluster0.yzosgks.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, tlsCAFile=ca)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

db = client.flask_db
todos = db.todos
#meganclapinski
#SUkH8z1RvqKcFJep

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        priority = request.form['priority']
        todos.insert_one({'content': content, 'priority': priority})
        return redirect(url_for('index'))

    all_todos = todos.find() # Add this line outside the if block! 
    return render_template('index.html', todos=all_todos) # add todos here! 
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))