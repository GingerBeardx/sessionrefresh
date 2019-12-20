"""
A simple project to refresh my meory on sessoin usage by creating a simple login
application.

Started December 18, 2019
Author: Eric Greenhalgh
"""

from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'yourenevertooyoung'


@app.route('/')
def index():
    if session['first_name'] not in session:
        session['first_name'] = []
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/regcheck', methods=['POST'])
def regcheck():
    # Check the form fields and make sure data was entered
    form_info = request.form
    # If data was not entered flash message that both fields must be filled out
    if len(form_info['first_name']) < 2 or len(form_info['last_name']) < 2:
        flash('Names must be at least 2 characters long', 'danger')
        return redirect('register')
    else:
        # If data was entered flash a message thanking the user for the info
        session['first_name'] = form_info['first_name']
        flash(
            f'Thank you for the information, {session["first_name"]}', 'success')
        return redirect('register')


@app.route('/active')
def active():
    return render_template('active.html')


if __name__ == '__main__':
    app.run(debug=True)
