from flask import Blueprint, render_template, request
from database.db_connection import run_query

# Create a blueprint for participants routes
participants_bp = Blueprint('participants', __name__)

@participants_bp.route('/participants', methods=['GET', 'POST'])
def renderParticipants():
    events = run_query("SELECT * FROM events;")

    if request.method == "POST":
        Event = request.form['Event']
        participants = run_query(f"SELECT p_id, fullname, mobile, email FROM participants WHERE event_id={Event}")
        return render_template('participants.html', events=events, participants=participants)

    return render_template('participants.html', events=events)