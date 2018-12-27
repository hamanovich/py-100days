from flask import Flask, render_template, flash, redirect, url_for
from config import Config

from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

print(app.config['SECRET_KEY'])


@app.route('/')
def index():
    return render_template('index.html', title='Home page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


if __name__ == "__main__":
    app.run()
