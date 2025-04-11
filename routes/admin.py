from flask import Blueprint, render_template, request, redirect
from database.db_connection import run_query

# Create a blueprint for admin routes
admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def renderAdmin():
    if request.method == 'POST':
        UN = request.form['username']
        PS = request.form['password']

        # Use run_query to fetch admin credentials
        cred = run_query("SELECT * FROM admin")
        for user in cred:
            if UN == user[0] and PS == user[1]:
                return redirect('/eventType')

        return render_template('admin.html', errors=["Wrong Username/Password"])

    return render_template('admin.html')