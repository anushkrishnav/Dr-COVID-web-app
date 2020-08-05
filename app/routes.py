from flask import render_template,redirect
from app import app
@app.route('/')
def redir():
    return redirect('/index')
@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html',index=True)