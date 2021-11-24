from datetime import datetime
from flask import Flask, render_template, request
from pymongo.response import Response
from database import database
import pprint

app = Flask(__name__)
database.initialize_db()

@app.route("/")
def home():
    return render_template(
        "home.html", data=database.find_tasks(0)
    )

@app.route("/viewtask/<string:task_id>", methods=['GET'])
def view_task(task_id):
    return render_template(
        "viewtask.html", data=database.find_task(task_id)
    )

@app.route("/edittask/<string:task_id>", methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'GET':
        return render_template(
            "edittask.html", data=database.find_task(task_id)
        )
    if request.method == 'POST':
        data = database.find_task(request.view_args['task_id'])
        data['name'] = request.form['name']
        data['description'] = request.form['description']
        data['due'] = request.form['due']
        if 'completed' in request.form.keys():
            data['completed'] = True
            
        database.update_task(data)
        
        return view_task(request.view_args['task_id'])