from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import init_db, User, Todo, db
from controllers import (login_controller, register_controller,
                         add_todo_controller, edit_todo_controller,
                         delete_todo_controller, toggle_todo_controller)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key' # Thay bằng key của bạn
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

# Khởi tạo database
db.init_app(app)
with app.app_context():
    init_db()

# Khởi tạo Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'

@login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

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

@app.route('/', methods=['GET', 'GET'])
@login_required
def index():
    filter_status = request.args.get('filter', 'all')
    todos = Todo.query.filter_by(user_id=current_user.id)
    if filter_status == 'completed':
        todos = todos.filter(Todo.status == True)
    elif filter_status == 'active':
        todos = todos.filter(Todo.status == False)
    todos = todos.all()
    return render_template('index.html', todos=todos, filter_status=filter_status)

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