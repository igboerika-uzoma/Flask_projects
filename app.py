from flask import Flask
from flask import render_template
form flask import request


app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/Login')
def signup():
    return render_template('Login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/guests')
def guest_page():
    return render_template('guests.html')


@app.route('/books')
def books():
    return render_template('bookslist.html')

@app.route('/generalinfo')
def general_info():
    return render_template('general_info.html')


@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/changepassword')
def change_password():
    return render_template('change_password.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_page')
def admin_page():
    return render_template('admin_page.html')

@app.route('/add_books')
def add_book():
    return render_template('add_books.html')

@app.route('/Remove_book')
def Remove_book():
    return render_template('Remove_book.html')

