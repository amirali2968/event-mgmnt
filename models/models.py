from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Admin:
    """Admin model class"""
    username: str
    password: str  # Note: In a real application, passwords should be hashed

@dataclass
class EventType:
    """Event type model class"""
    type_id: int
    type_name: str
    description: str
    participant_count: Optional[int] = 0

@dataclass
class Event:
    """Event model class"""
    event_id: int
    type_id: int
    event_name: str
    event_date: datetime
    location: str
    description: str
    available_seats: int
    total_seats: int

@dataclass
class Participant:
    """Participant model class"""
    participant_id: int
    event_id: int
    name: str
    email: str
    phone: str
    registration_date: datetime