from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, current_user
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Firebase setup
cred = credentials.Certificate('firebase-credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register-college')
def register_college():
    return render_template('register_college.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
