from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
    'author': 'Kelvin Beno',
    'title': 'Blog post 1',
    'content':'First post content',
    'date_posted':'January 26, 2019'
    },
    {

    'author': 'Everlyn Kihara',
    'title': 'Blog post 2',
    'content':'Second post content',
    'date_posted':'January 27, 2019'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
