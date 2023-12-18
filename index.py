from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from pymongo import MongoClient


app = Flask(__name__, template_folder='../Myst', static_folder='static')
app.secret_key = 'your_secret_key'  # Cambia con una chiave segreta più sicura
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo
usersCollection = db.users

@app.route('/')
@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/index.html')
def index():

    return render_template('index.html')

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = usersCollection
        signup_user = users.find_one({'username': request.form['username']})

        if signup_user:
            flash(request.form['username'] + ' username is already exist')
            return redirect(url_for('signup'))

    
        users.insert_one({'username': request.form['username'], 'password': request.form['password'], 'email': request.form['email']})

        session['username'] = request.form['username']
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = db.users
        signin_user = users.find_one({'username': request.form['username'],'password':request.form['password']})

        if signin_user:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        flash('Username and password combination is wrong')
        return url_for('index')

    return render_template('login.html')

@app.route('/giocoAce')
def Ace():
    return render_template('giocoAce.html')


@app.route('/giocoAmongUs')
def Among():
    return render_template('giocoAmongUs.html')

@app.route('/giocoBaldur')
def Baldur():
    return render_template('giocoBaldur.html')


@app.route('/giocoCS2')
def CS2():
    return render_template('giocoCS2.html')

@app.route('/giocoMirror')
def Mirror():
    return render_template('giocoMirror.html')

@app.route('/giocoNier')
def Nier():
    return render_template('giocoNier.html')

@app.route('/giocoOT')
def OT():
    return render_template('giocoOT.html')

@app.route('/giocoPersona5')
def Persona5():
    return render_template('giocoPersona5.html')

@app.route('/giocoStardew')
def Stardew():
    return render_template('giocoStardew.html')

@app.route('/giocoTunic')
def Tunic():
    return render_template('giocoTunic.html')

if __name__ == "__main__":
    app.run(debug=True)
