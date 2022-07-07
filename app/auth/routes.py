from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from .forms import LoginForm, SignupForm, EditProfile
from .models import db, User
from .. import login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash
from app import app

login_manager.login_view = "login"

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    profile_form = EditProfile(email=current_user.email, address=current_user.address)
    if profile_form.validate_on_submit():
        user = User.query.get(current_user.id)
        if user.check_password(profile_form.password.data):
            if current_user.email != profile_form.email.data:
                if User.query.filter_by(email=profile_form.email.data).first() is None:
                    user.email = profile_form.email.data
                else:
                    flash('Email already in use.')
            if current_user.address != profile_form.address.data:
                user.address = profile_form.address.data
            if current_user.password != generate_password_hash(profile_form.newpassword.data, method='pbkdf2:sha512:200000'):
                user.set_password(profile_form.newpassword.data)
            if profile_form.delete.data:
                db.session.delete(user)
            db.session.commit()
            return redirect(url_for('profile'))
    return render_template('profile.html', title='edit profile', form=profile_form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password=password):
            login_user(user)
            return redirect(url_for('index'))
        flash("Doesn't seem quite right. Try again?")
    return render_template('login.html', form=login_form, title='login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        email = signup_form.email.data
        if User.query.filter_by(email=email).first() is None:
            if signup_form.address.data:
                user = User(email=email, address=signup_form.address.data)
            else:
                user = User(email=email)
            user.set_password(signup_form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Email already in use. Try logging in?')
    signup_form.terms.data = False
    return render_template('signup.html', title='sign up', form=signup_form)

@app.route('/basket', methods=['GET', 'POST'])





@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.')
    return redirect(url_for('login'))
