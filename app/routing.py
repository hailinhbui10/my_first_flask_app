from flask import render_template, redirect, request
from app import app
from app import db
from app.models import Todo 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content= task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Something is wrong"
    else:
        tasks = Todo.query.order_by(Todo.date_utc).all()
        return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    deleted_task = Todo.query.get_or_404(id)

    try:
        db.session.delete(deleted_task)
        db.session.commit()
        return redirect('/')
    except:
        return "Something is wrong while deleting the task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Something is wrong while updating the task"
    else:
        return render_template('update.html', task = task)