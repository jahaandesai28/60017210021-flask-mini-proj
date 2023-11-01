from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a dictionary to store the tasks
tasks = {}

# Create a dictionary to store the categories
categories = {}

# Define the home page
@app.route('/')
def home():
    return render_template('home.html', tasks=tasks, categories=categories)

# Define the add task page
@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        category = request.form['category']
        tasks[task_name] = category
        if category not in categories:
            categories[category] = []
        categories[category].append(task_name)
        return redirect(url_for('home'))
    else:
        return render_template('add_task.html', categories=categories)

# Define the delete task page
@app.route('/delete_task', methods=['GET', 'POST'])
def delete_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        category = tasks[task_name]
        categories[category].remove(task_name)
        del tasks[task_name]
        return redirect(url_for('home'))
    else:
        return render_template('delete_task.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
