from flask import Flask, jsonify, make_response

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
    if len(task) == 0:
        abort(404)
    
    return jsonify({"task": tasks})

@app.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_by_id(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    
    if len(task) == 0:
        not_found(404)
    
    return jsonify({'task': task[0]})

## error handling 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)