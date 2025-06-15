from flask import flash, redirect
from models import User, Todo
from werkzeug.security import generate_password_hash

def login_controller(request, render_template, check_password_hash, login_user, url_for):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

def register_controller(request, render_template, generate_password_hash, url_for):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
    return render_template('register.html')

def add_todo_controller(request, current_user, db, url_for):
    title = request.form['title']
    if title:
        new_todo = Todo(title=title, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

def edit_todo_controller(request, id, db, current_user, url_for):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('Unauthorized action')
        return redirect(url_for('index'))
    title = request.form['title']
    if title:
        todo.title = title
        db.session.commit()
    return redirect(url_for('index'))

def delete_todo_controller(id, db, current_user, url_for):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('Unauthorized action')
        return redirect(url_for('index'))
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

def toggle_todo_controller(id, db, current_user, url_for):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('Unauthorized action')
        return redirect(url_for('index'))
    todo.status = not todo.status
    db.session.commit()
    return redirect(url_for('index'))