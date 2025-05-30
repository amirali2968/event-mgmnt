from flask import Blueprint, render_template, request
from services.event_service import EventTypeService

# Create a blueprint for event type routes
event_type_bp = Blueprint('event_type', __name__)

@event_type_bp.route('/eventType', methods=['GET', 'POST'])
def getEvents():
    # Use the event type service to get all event types
    event_types = EventTypeService.get_all_event_types()
    
    return render_template('events.html', eventTypes=event_types)