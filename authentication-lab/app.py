from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
  "apiKey": "AIzaSyBsWDq5JrfvQpZ7qjzeFHrMK903h_m5eqo",
  "authDomain": "iasafood.firebaseapp.com",
  "projectId": "iasafood",
  "storageBucket": "iasafood.appspot.com",
  "messagingSenderId": "1092894316925",
  "appId": "1:1092894316925:web:2216a4fc39458d1c87d414",
  "measurementId": "G-ZGX9XWSYGS",
  "databaseURL": "",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session["user"] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for("add_tweet"))
        except:
            error = "signin failed"
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        try:
            login_session["user"] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for("add_tweet"))
        except:
            error = "signup failed"
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)