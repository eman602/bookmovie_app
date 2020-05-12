from flask import Flask, render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home Page")

@app.route('/about')
def about():
    return render_template('about.html', title="About Page")



@app.route('/book')
def book():
    return render_template('book.html', title="Book Page")


@app.route('/movie')
def movie():
    return render_template('movie.html', title="Movie Page")


@app.route('/register')
def register():
    return render_template('register.html', title="Register Page")


