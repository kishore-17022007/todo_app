from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample todo list (can be replaced with a database or other storage)
todos = [
    {'task': 'Complete assignment', 'done': False},
    {'task': 'Go for a run', 'done': True},
    {'task': 'Buy groceries', 'done': False}
]

# Route to render the todo list
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# Route to add a new todo item
@app.route('/add', methods=['POST'])
def add_todo():
    new_todo = request.form.get('todo')
    todos.append({'task': new_todo, 'done': False})
    return redirect(url_for('index'))

# Route to edit a todo item
@app.route('/edit/<int:index>')
def edit(index):
    todo_to_edit = todos[index]
    return render_template('edit.html', index=index, todo=todo_to_edit)

# Route to update a todo item
@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    updated_todo = request.form.get('todo')
    todos[index]['task'] = updated_todo
    return redirect(url_for('index'))

# Route to delete a todo item
@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)