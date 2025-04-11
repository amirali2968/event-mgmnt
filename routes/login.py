from flask import Blueprint, render_template, request
from database.db_connection import run_query

# Create a blueprint for login routes
login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def renderLoginPage():
    events = run_query("SELECT * FROM events")
    branch = run_query("SELECT * FROM branch")
    if request.method == 'POST':
        Name = request.form['FirstName'] + " " + request.form['LastName']
        Mobile = request.form['MobileNumber']
        Branch_id = request.form['Branch']
        Event = request.form['Event']
        Email = request.form['Email']

        if len(Mobile) != 10:
            return render_template('loginfail.html', errors=["Invalid Mobile Number!"])

        if Email[-4:] != '.com':
            return render_template('loginfail.html', errors=["Invalid Email!"])

        if len(run_query(f"SELECT * FROM participants WHERE event_id={Event} AND mobile={Mobile}")) > 0:
            return render_template('loginfail.html', errors=["Student already Registered for the Event!"])

        if run_query(f"SELECT COUNT(*) FROM participants WHERE event_id={Event}") >= run_query(f"SELECT participants FROM events WHERE event_id={Event}"):
            return render_template('loginfail.html', errors=["Participants count fulfilled Already!"])

        run_query(f"INSERT INTO participants(event_id, fullname, email, mobile, college, branch_id) VALUES({Event}, \"{Name}\", \"{Email}\", \"{Mobile}\", \"COEP\", \"{Branch_id}\");", fetch_results=False)

        return render_template('index.html', events=events, branchs=branch, errors=["Successfully Registered!"])

    return render_template('index.html', events=events, branchs=branch)