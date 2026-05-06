from flask import Blueprint, render_template, request, redirect, url_for, jsonify, current_app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User, db
import random

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('login_id')
        password = request.form.get('login_password')

        user = User.query.filter_by(username=username).first()

        if user :
            if check_password_hash(user.password, password):
                login_user(user=user, remember=True)
                return redirect(url_for('views.home'))
            else :
                print("Incorrect email or password")
        else :
            print("Account not found!")

    return render_template('login.html')

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('n_email')
        username = request.form.get('n_username')

        name = request.form.get('n_name')
        password = request.form.get('n_password')

        user_email = User.query.filter_by(email=email).first()
        user_username = User.query.filter_by(username=username).first()

        if user_email and not user_username :
            return "Email already in use"
        elif user_username and not user_email:
            return "Username already Taken"
        elif user_email and user_username:
            return "Account exists already"
        else :
            new_user = User(name=name, username=username, email=email, password=generate_password_hash(password=password, method='scrypt'),
                            col_r=random.randint(0, 255), col_g=random.randint(0, 255), col_b=random.randint(0, 255)
                            )
            db.session.add(new_user)
            db.session.commit()
            login_user(user=new_user, remember=True)
            print("User Created!")
            return redirect(url_for('views.home'))

    return render_template('sign-up.html')

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
