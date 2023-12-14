from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo
usersCollection = db.users

@app.route("/")
@app.route("/main")
def main():
    return render_template('/index.html')

@app.route("/signup.html", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = usersCollection
        signup_user = users.find_one({'username': request.form['username']})

        if signup_user:
            flash(request.form['username'] + ' username is already exist')
            return redirect(url_for('signup'))

        hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt(14))
        users.insert_one({'username': request.form['username'], 'password': hashed, 'email': request.form['email']})

        session['username'] = request.form['username']
        return redirect(url_for('/index.html'))

    return render_template('/signup.html')
@app.route('/index.html')
def index():
    if 'username' in session:
        return render_template('/index.html')

    return render_template('/index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        users = db.users
        signin_user = users.find_one({'username': request.form['username']})

        if signin_user and bcrypt.checkpw(request.form['password'].encode('utf-8'), signin_user['password']):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        flash('Username and password combination is wrong')
        return render_template('login.html')

    return render_template('/login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
