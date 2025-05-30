from flask import Blueprint, render_template, request, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from services.admin_service import AdminService

# Create a form class for admin login
class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Create a blueprint for admin routes
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def renderAdmin():
    form = AdminLoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Use the admin service for authentication
        if AdminService.authenticate(username, password):
            # Set session variables for logged-in admin
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect('/eventType')

        return render_template('admin.html', form=form, errors=["Wrong Username/Password"])

    return render_template('admin.html', form=form)