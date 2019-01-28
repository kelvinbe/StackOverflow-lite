from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '6068758f589fd21f74dd31a4694faa13'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kelvin:5000@localhost/stackdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String('12345'), nullable=False)
    post_question = db.relationship('Post', lazy=True)
    post_answer = db.relationship('Post', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

'''
class Post_question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.text, nullable=False)
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post_answer('{self.title}', '{self.date_posted}')"
'''

'''class Post_answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.text, nullable=False)
    user_id = db.Column(db.Integer, db.Foreignkey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post_answer('{self.title}', '{self.date_posted}')"
'''




posts = [
    {
    'author': 'Kelvin Beno',
    'title': 'Question 1',
    'content':'What is a variable?',
    'date_posted':'January 26, 2019'
    },
    {

    'author': 'Everlyn Kihara',
    'title': 'Question 2',
    'content':'Is Javascript linked to Java?',
    'date_posted':'January 27, 2019'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 
            'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)






