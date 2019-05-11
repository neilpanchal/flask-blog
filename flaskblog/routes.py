from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Neil Smith',
        'title': 'Blog Post 1',
        'content': 'Systems, in one sense, are devices that take input and produce an output. A system can be thought to operate on the input to produce the output. The output is related to the input by a certain relationship known as the system response. The system response usually can be modeled with a mathematical relationship between the system input and the system output.',
        'date_posted': 'Apr 20, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content':'The fundamental concepts of classical physics, space, time, mass, and derived concepts, velocity, momentum, force, angular momentum, energy ... all rest on the principle that material points have trajectories. They are defined as lines in space-time. Even the dynamics of continuous, solid or fluid media describes the trajectories of the material points which constitute the bodies in motion. How then can it explain all the appearances which legitimize the fundamental concepts of classical physics?',
        'date_posted': 'Apr 22, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', data = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','green')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'green')
            return redirect(url_for('home'))
        else:
            flash(f'Please check username and/or password!', 'red')

    return render_template('login.html', title = 'Login', form=form)
