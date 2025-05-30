# Event Management System

## Project Overview
This is a Flask-based event management system that allows administrators to manage events and participants. The system has been restructured to follow a modular architecture with clear separation of concerns.

## Project Structure

```
event-management-system/
├── app.py                  # Application entry point
├── config.py               # Configuration management
├── database/               # Database connection and utilities
│   ├── db_connection.py    # Database connection pool and query functions
│   └── events.sql          # Database schema
├── models/                 # Data models
│   ├── __init__.py
│   └── models.py           # Entity models (Admin, Event, EventType, Participant)
├── routes/                 # Route handlers
│   ├── admin.py            # Admin routes
│   ├── event_info.py       # Event information routes
│   ├── event_type.py       # Event type routes
│   ├── login.py            # User login routes
│   └── participants.py     # Participant management routes
├── services/               # Business logic
│   ├── __init__.py
│   ├── admin_service.py    # Admin authentication service
│   └── event_service.py    # Event and event type services
├── static/                 # Static assets
│   └── images/             # Image files
└── templates/              # HTML templates
    ├── admin.html          # Admin login page
    ├── events.html         # Event listing page
    ├── events_info.html    # Event details page
    ├── index.html          # Homepage
    ├── loginfail.html      # Login failure page
    └── participants.html   # Participants management page
```

## Architecture

The project follows a layered architecture:

1. **Models Layer**: Defines data structures using dataclasses
2. **Services Layer**: Contains business logic and database operations
3. **Routes Layer**: Handles HTTP requests and responses
4. **Database Layer**: Manages database connections and query execution
5. **Configuration**: Centralizes application settings

## Setup Instructions

### Prerequisites
- Python 3.7+
- MySQL database

### Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```
   mysql -u root -p < database/events.sql
   ```
4. Configure environment variables (optional):
   ```
   export FLASK_ENV=development
   export DB_HOST=localhost
   export DB_NAME=event_mgmt
   export DB_USER=root
   export DB_PASSWORD=your_password
   ```

### Running the Application

```
python app.py
```

The application will be available at http://localhost:5000

## Docker Setup

Alternatively, you can use Docker Compose to run the application:

```
docker-compose up
```

## Security Considerations

- The current implementation uses plain text passwords, which should be replaced with proper password hashing in a production environment
- SQL injection protection is implemented using parameterized queries
- Session management is handled by Flask's session mechanism
