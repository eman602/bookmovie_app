from flask import Flask, render_template, redirect, url_for
from application import app, db
from application.models import Books, Movies
from application.forms import BookForm, MovieForm, BookUpdate, BookUpdate2

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form=BookUpdate()
    if form.validate_on_submit():
        book_details=Books.query.filter_by(book_name=form.search_book.data).first()
        if book_details:
            return redirect(url_for('update'))
    return render_template('home.html', title="Home Page", form=form)

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


@app.route('/update')
def update():
    return render_template('update.html', title="UpdatePage")

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


app.route('/update', methods=['GET', 'POST'])
def addingupdates():
    form = BookUpdate2()
    if form.validate_on_submit():
        postData = Books(
            book_name = form.book_name.data,
            author_name = form.author_name.data,
            genre = form.genre.data,
            short_content = form.short_content.data
        )
        db.session.commit()
    elif request.method=='GET':
        form.book_name.data = book_name
        form.author_name.data = author_name
        form.genre.data = genre
        form.short_content.data = short_content
        
        return redirect(url_for('book'))
    return render_template('update.html', title='Dost', form=form)




















