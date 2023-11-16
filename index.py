from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo
usersCollection = db.users

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user_data = {
            'username': username,
            'email': email,
            'password': password
        }

        result = usersCollection.insert_one(user_data)
        inserted_id = result.inserted_id

        return f"User registered with ID: {inserted_id}"

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
