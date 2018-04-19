from flask import url_for, redirect, render_template, flash
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('auth/login.html', title='Sign In', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))
