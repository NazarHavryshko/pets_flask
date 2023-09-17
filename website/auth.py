from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

from .models import Users
from . import db
from .validations import UserInformationValidation

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect by password, try again.', category='error')
        else:
            flash('Email is not exist.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        email = request.form['email']
        password1 = request.form['password1']
        password2 = request.form['password2']
        name = request.form.get('name')

        user = Users.query.filter_by(email=email).first()
        uiv = UserInformationValidation()

        if user:
            flash('This email already exists', category='error')
            return redirect(url_for('auth.registration'))

        elif password1 != password2:
            flash('You need to enter the same passwords', category='error')
            return redirect(url_for('auth.registration'))

        elif not uiv.validation_email(email):
            flash('This email is not correct (Example: test@gmail.com)', category='error')
            return redirect(url_for('auth.registration'))

        elif not uiv.validation_password(password1):
            flash('This password is not correct (Example: 123QWErty123)', category='error')
            return redirect(url_for('auth.registration'))

        elif not uiv.validation_name(name):
            flash('This name is not correct (Example: Alina)', category='error')
            return redirect(url_for('auth.registration'))

        else:
            new_user = Users(
                username=name,
                email=email,
                password=generate_password_hash(password1, method='scrypt'),
                birthday=date.today(),
                phoneNumber='+380000000000',
                city='None'
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            return redirect(url_for('views.index'))

    return render_template('registration.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))
