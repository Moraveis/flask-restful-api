from flask import Flask, jsonify, request, make_response, abort
#from flask import make_response

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": u"Buy Groceries",
        "description": u"Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False
    },
    {
        "id": 2,
        "title": u"Learn Python",
        "description": u"Need to find a good Python tutorial on the web",
        "done": False
    },
]

@app.route("/api/v1/tasks", methods=['GET'])
def get():
    if len(tasks) == 0:
        abort(404)
    
    return jsonify({"task": tasks})

@app.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_by_id(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    
    if len(task) == 0:
        abort(404)
    
    return jsonify({'task': task[0]})

@app.route('/api/v1/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    
    task = { 
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({'task': task}), 201

## error handling 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)