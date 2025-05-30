from database.db_connection import run_query
from models.models import EventType, Event, Participant
from typing import List, Optional, Dict, Any

class EventTypeService:
    """Service class for event type operations"""
    
    @staticmethod
    def get_all_event_types() -> List[EventType]:
        """
        Get all event types with participant counts.
        
        Returns:
            List[EventType]: List of event types
        """
        query = """
            SELECT *,
                   (SELECT COUNT(*) 
                    FROM participants AS P 
                    WHERE T.type_id IN (SELECT type_id FROM events AS E WHERE E.event_id = P.event_id)) AS COUNT
            FROM event_type AS T;
        """
        results = run_query(query)
        event_types = []
        
        for row in results:
            event_types.append(EventType(
                type_id=row[0],
                type_name=row[1],
                description=row[2],
                participant_count=row[3]
            ))
        
        return event_types
    
    @staticmethod
    def get_event_type_by_id(type_id: int) -> Optional[EventType]:
        """
        Get event type by ID.
        
        Args:
            type_id: Event type ID
            
        Returns:
            Optional[EventType]: Event type if found, None otherwise
        """
        query = "SELECT * FROM event_type WHERE type_id = %s;"
        result = run_query(query, (type_id,))
        
        if result and len(result) > 0:
            row = result[0]
            return EventType(
                type_id=row[0],
                type_name=row[1],
                description=row[2]
            )
        
        return None

class EventService:
    """Service class for event operations"""
    
    @staticmethod
    def get_events_by_type(type_id: int) -> List[Event]:
        """
        Get all events of a specific type.
        
        Args:
            type_id: Event type ID
            
        Returns:
            List[Event]: List of events
        """
        query = "SELECT * FROM events WHERE type_id = %s;"
        results = run_query(query, (type_id,))
        events = []
        
        for row in results:
            events.append(Event(
                event_id=row[0],
                type_id=row[1],
                event_name=row[2],
                event_date=row[3],
                location=row[4],
                description=row[5],
                available_seats=row[6],
                total_seats=row[7]
            ))
        
        return events