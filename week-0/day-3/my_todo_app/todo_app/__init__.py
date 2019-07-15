import os

from flask import Flask
from flask import request

from flask import render_template

todo_store = {}
todo_store['shivang'] = ['Wake Up', 'Drink Coffee', 'Read Non-fiction Novel'] 
todo_store['shubham'] = ['Wake Up', 'Drink Coffee', 'Read']
todo_store['saurabh'] = ['Wake Up', 'Drink Coffee', 'Read']
todo_store['juhi']    = ['dancing', 'cooking']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name) :
        global todo_store
        return todo_store[name]

    def insert_todo(name, todo):
      global todo_store
      current_todos = todo_store[name]
      current_todos.append(todo)
      todo_store[name] = current_todos 

    def add_todo_by_name(name, todo):
      insert_todo(name, todo)
      return
   
    def get_todo_by_name(name):
      try:
       return select_todos(name)
      except:
       return None

    @app.route('/todos')
    def todos():
       name = request.args.get('name')
       print('-----')
       print(name)
       print('----')

       person_todo_list = get_todo_by_name(name)

       if(person_todo_list == None):
        return render_template('404.html'),404
       else:
        return render_template('todo_view.html',todos=person_todo_list)

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name, todo)

        return 'Added Successfully'

    return app