from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Book
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev-secret-change-me'

# initialize db with app
db.init_app(app)

# Create DB tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect(url_for('book_list'))

@app.route('/books')
def book_list():
    books = Book.query.order_by(Book.id).all()
    return render_template('book_list.html', books=books)

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        year = request.form.get('year', '').strip()
        isbn = request.form.get('isbn', '').strip()

        if not title:
            flash('Title is required.', 'error')
            return render_template('add_book.html')
        
        book = Book(title=title, author=author or None,
                    year=int(year) if year.isdigit() else None,
                    isbn=isbn or None)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully.', 'success')
        return redirect(url_for('book_list'))
    
    return render_template('add_book.html')

@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        year = request.form.get('year', '').strip()
        isbn = request.form.get('isbn', '').strip()

        if not title:
            flash('Title is required.', 'error')
            return render_template('edit_book.html', book=book)
        
        book.title = title
        book.author = author or None
        book.year = int(year) if year.isdigit() else None
        book.isbn = isbn or None
        db.session.commit()
        flash('Book updated.', 'success')
        return redirect(url_for('book_list'))
    
    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted.', 'success')
    return redirect(url_for('book_list'))


if __name__ == '__main__':
    app.run(debug=True)