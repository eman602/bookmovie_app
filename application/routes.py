from flask import Flask, render_template, redirect, url_for
from application import app, db
from application.models import Books, Movies
from application.forms import BookForm, MovieForm

@app.route('/')
@app.route('/home')
def home():
    bookData=Books.query.all()
    return render_template('home.html', title="Home Page", posts=bookData)

@app.route('/about')
def about():
    return render_template('about.html', title="About Page")



@app.route('/book')
def book():
    bookData=Books.query.all()
    return render_template('book.html', title="Book Page", posts=bookData)


@app.route('/movie')
def movie():
    movieData=Movies.query.all()
    return render_template('movie.html', title="Movie Page", dosts=movieData)


@app.route('/register')
def register():
    return render_template('register.html', title="Register Page")

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = BookForm()
    if form.validate_on_submit():
        postData = Books(
            book_name = form.book_name.data,
            author_name = form.author_name.data,
            genre = form.genre.data,
            short_content = form.short_content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('book'))

    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=form)


@app.route('/dost', methods=['GET', 'POST'])
def dost():
    form = MovieForm()
    if form.validate_on_submit():
        postData2 = Movies(
            movie_name = form.movie_name.data,
            director_name = form.director_name.data,
            genre = form.genre.data,
            short_content = form.short_content.data,
            book_id=form.book_id.data
        )

        db.session.add(postData2)
        db.session.commit()

        return redirect(url_for('movie'))

    else:
        print(form.errors)

    return render_template('dost.html', title='Dost', form=form)


