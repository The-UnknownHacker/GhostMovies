from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required,logout_user
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

class User(UserMixin):
    pass

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'

def get_db_connection():
    db = sqlite3.connect('database.db')
    db.row_factory = sqlite3.Row
    return db

@login_manager.user_loader
def load_user(user_id):
    db = get_db_connection()
    user_data = db.execute('SELECT * FROM users WHERE username = ?', (user_id,)).fetchone()
    db.close()

    if user_data:
        user = User()
        user.id = user_id
        return user
    return None


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/watch')
@login_required
def watch():
    return render_template('watch.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None  # Initialize an error variable
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db_connection()
        user_data = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        db.close()

        if user_data and check_password_hash(user_data['password'], password):
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('watch'))
        else:
            error = 'Invalid username or password'  # Set error message

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']

        db = get_db_connection()
        try:
            db.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
            db.commit()
        except sqlite3.IntegrityError:
            # Handle error: username already exists
            pass
        finally:
            db.close()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
@login_required    
def logout():
    logout_user()
    return redirect(url_for('login'))

def init_db():
    db = get_db_connection()
    db.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, email TEXT)')
    db.commit()
    db.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
