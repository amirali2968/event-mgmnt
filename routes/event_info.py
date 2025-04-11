from flask import Blueprint, render_template
from database.db_connection import run_query  # Updated function name

# Create a blueprint for event info routes
event_info_bp = Blueprint('event_info', __name__)

@event_info_bp.route('/eventinfo')
def renderEventInfo():
    """
    Render the event information page.
    """
    # Query to fetch event details along with participant count
    events = run_query("""
        SELECT *,
               (SELECT COUNT(*) 
                FROM participants AS P 
                WHERE P.event_id = E.event_id) AS count
        FROM events AS E
        LEFT JOIN event_type USING(type_id)
        LEFT JOIN location USING(location_id);
    """)
    return render_template('events_info.html', events=events)