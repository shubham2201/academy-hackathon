import os


from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    def todo_view(todos):
        the_view = 'List of my Todos' + '<br>'
        for todo in todos:
            the_view += (todo + '<br>')

        the_view += ('--End--')
        return the_view

   
    def get_todo_by_name(name) :
       if name == 'shivang':
        return ['Wake Up', 'Drink Coffee', 'Read Non-fiction Novel']      
       elif name == 'shubham':
        return ['Wake Up', 'Drink Coffee', 'Read']
       elif name == 'saurabh':
        return ['Wake Up', 'Drink Coffee', 'Read']
       elif name == 'juhi' :
        return ['dancing', 'cooking']
       else :
        return []


    @app.route('/todos')
    def todos():
       name = request.args.get('name')
       print('-----')
       print(name)
       print('----')

       person_todo_list = get_todo_by_name(name)
       return todo_view(person_todo_list) 

    return app