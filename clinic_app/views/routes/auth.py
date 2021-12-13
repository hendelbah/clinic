"""
Authentication routes
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required

from clinic_app.views.api_controllers import ApiHelper
from clinic_app.views.forms import LoginForm, ChangePassForm
from clinic_app.views.user_login import UserLogin

auth_bp = Blueprint('auth', __name__)


# pylint: disable=missing-function-docstring
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('general.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = UserLogin.load_by_email(form.email.data)
        if user and user.check_password(form.pwd.data):
            login_user(user, remember=form.remember.data)
            flash('You successfully logged in', 'success')
            return redirect(request.args.get('next') or url_for('general.index'))
        flash('Wrong email or password', 'error')
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You successfully logged out', 'success')
        return redirect(url_for('general.index'))
    flash('You are not logged in to log out', 'warning')
    return redirect(request.args.get('next') or url_for('general.index'))


@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ChangePassForm()
    if form.is_submitted():
        if form.validate() and current_user.check_password(form.password.data):
            pass_hash = UserLogin.hash_password(form.password.data)
            data = {'password_hash': pass_hash}
            response = ApiHelper.user.put(current_user.uuid, data=data)
            if response.status_code == 200:
                flash('Your password was changed', 'success')
            else:
                flash('Password change failed', 'error')
        else:
            flash('Wrong password or new passwords don\'t match', 'error')
    return render_template('profile.html', form=form)
