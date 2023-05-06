from flask import Blueprint, render_template, redirect, url_for, flash, get_flashed_messages

from .forms import RegistrationForm, LoginForm


admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Created account for {form.username.data}!', 'success')
        return redirect(url_for('admin_bp.login'))
    else:
        flash('Invalid options')
    return render_template('register.html', title='Auth | Sign up', form=form)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', title='Auth | Login', form=form)

