from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import init_db, User, Todo, db
from controllers import (login_controller, register_controller,
                         add_todo_controller, edit_todo_controller,
                         delete_todo_controller, toggle_todo_controller)
from math import ceil
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Khởi tạo database
db.init_app(app)
with app.app_context():
    init_db()
    # Thêm người dùng mẫu
    if not User.query.first():  # Chỉ thêm nếu chưa có người dùng
        user = User(username='user1', password=generate_password_hash('123'))
        db.session.add(user)
        db.session.commit()
        # Thêm công việc mẫu
        todo = Todo(title='Sample Task', user_id=user.id)
        db.session.add(todo)
        db.session.commit()

# Khởi tạo Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_controller(request, render_template, check_password_hash, login_user, url_for)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return register_controller(request, render_template, generate_password_hash, url_for)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    # 1. Handle filter
    filter_status = request.args.get('filter', 'all')
    page = request.args.get('page', 1, type=int)
    per_page = 7

    # 2. Base query
    todos_query = Todo.query.filter_by(user_id=current_user.id)

    if filter_status == 'completed':
        todos_query = todos_query.filter(Todo.status == True)
    elif filter_status == 'active':
        todos_query = todos_query.filter(Todo.status == False)

    # 3. Total count and paginate
    total_todos = todos_query.count()
    todos = todos_query.order_by(Todo.id.desc()).offset((page - 1) * per_page).limit(per_page).all()
    total_pages = ceil(total_todos / per_page)

    return render_template('index.html',
                           todos=todos,
                           filter_status=filter_status,
                           page=page,
                           pages=total_pages)

@app.route('/add', methods=['POST'])
@login_required
def add():
    return add_todo_controller(request, current_user, db, url_for)

@app.route('/edit/<int:id>', methods=['POST'])
@login_required
def edit(id):
    return edit_todo_controller(request, id, db, current_user, url_for)

@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    return delete_todo_controller(id, db, current_user, url_for)

@app.route('/toggle/<int:id>', methods=['POST'])
@login_required
def toggle(id):
    return toggle_todo_controller(id, db, current_user, url_for)

if __name__ == '__main__':
    app.run(debug=True)