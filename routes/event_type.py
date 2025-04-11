from flask import Blueprint, render_template, request
from database.db_connection import run_query

# Create a blueprint for event type routes
event_type_bp = Blueprint('event_type', __name__)

@event_type_bp.route('/eventType', methods=['GET', 'POST'])
def getEvents():
    eventTypes = run_query("""
        SELECT *,
               (SELECT COUNT(*) 
                FROM participants AS P 
                WHERE T.type_id IN (SELECT type_id FROM events AS E WHERE E.event_id = P.event_id)) AS COUNT
        FROM event_type AS T;
    """)
    events = run_query("""
        SELECT event_id, event_title,
               (SELECT COUNT(*) 
                FROM participants AS P 
                WHERE P.event_id = E.event_id) AS count
        FROM events AS E;
    """)
    types = run_query("SELECT * FROM event_type;")
    location = run_query("SELECT * FROM location")

    if request.method == "POST":
        try:
            Name = request.form["newEvent"]
            fee = request.form["Fee"]
            participants = request.form["maxP"]
            Type = request.form["EventType"]
            Location = request.form["EventLocation"]
            Date = request.form['Date']
            run_query(f"""
                INSERT INTO events(event_title, event_price, participants, type_id, location_id, date)
                VALUES("{Name}", {fee}, {participants}, {Type}, {Location}, '{Date}');
            """, fetch_results=False)
        except:
            EventId = request.form["EventId"]
            run_query(f"DELETE FROM events WHERE event_id={EventId}", fetch_results=False)

    return render_template('events.html', events=events, eventTypes=eventTypes, types=types, locations=location)