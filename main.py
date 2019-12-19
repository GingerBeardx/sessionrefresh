"""
A simple project to refresh my meory on sessoin usage by creating a simple login
application.

Started December 18, 2019
Author: Eric Greenhalgh
"""

from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = 'yourenevertooyoung'


@app.route('/')
def index():
    print(session)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
