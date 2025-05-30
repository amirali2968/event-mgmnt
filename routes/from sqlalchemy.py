from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

@contextmanager
def transaction_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

# Usage example
with transaction_scope() as session:
    # Perform database operations
    event = session.query(Event).filter_by(id=event_id).with_for_update().first()
    if event.available_seats > 0:
        event.available_seats -= 1
        participant = Participant(user_id=user_id, event_id=event_id)
        session.add(participant)