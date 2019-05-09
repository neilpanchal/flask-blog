from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Neil Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Apr 20, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Apr 22, 2019'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', data = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

# Run it in debug mode for dev
if __name__ == '__main__':
    app.run(debug=True)

