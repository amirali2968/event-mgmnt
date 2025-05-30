"""Mock database connection module for testing without a real database connection.

This module provides mock implementations of the database functions to allow
testing the application logic without requiring a real MySQL server connection.
"""

# Mock data for testing
MOCK_DATA = {
    'event_type': [
        (1, 'Conference', 'Professional gathering for discussions and networking'),
        (2, 'Workshop', 'Hands-on learning session'),
        (3, 'Seminar', 'Educational event with focus on specific topics'),
        (4, 'Webinar', 'Online seminar or presentation'),
        (5, 'Exhibition', 'Display of products, services, or information')
    ],
    'events': [
        (1, 'Annual Tech Conference', '2023-12-15', '2023-12-17', 'Main Convention Center', 1, 'Annual technology conference'),
        (2, 'Data Science Workshop', '2023-11-10', '2023-11-10', 'Innovation Hub', 2, 'Workshop on data science fundamentals'),
        (3, 'Leadership Seminar', '2024-01-20', '2024-01-21', 'Business Center', 3, 'Seminar on leadership skills')
    ],
    'participants': [
        (1, 1, 'John Doe', 'john@example.com', '555-123-4567'),
        (2, 1, 'Jane Smith', 'jane@example.com', '555-987-6543'),
        (3, 2, 'Bob Johnson', 'bob@example.com', '555-456-7890')
    ]
}

# Mock connection pool
class MockConnectionPool:
    def get_connection(self):
        return MockConnection()

# Mock connection
class MockConnection:
    def is_connected(self):
        return True
        
    def cursor(self, buffered=True):
        return MockCursor()
        
    def commit(self):
        pass
        
    def rollback(self):
        pass
        
    def close(self):
        pass

# Mock cursor
class MockCursor:
    def __init__(self):
        self.results = []
        self.last_query = ""
        self.last_params = None
        
    def execute(self, query, params=None):
        self.last_query = query.strip().upper()
        self.last_params = params
        
        # Handle different query types
        if self.last_query.startswith('SELECT'):
            self._handle_select(query, params)
        elif self.last_query.startswith('INSERT'):
            self._handle_insert(query, params)
        elif self.last_query.startswith('DELETE'):
            self._handle_delete(query, params)
        
    def _handle_select(self, query, params):
        # Extract table name from query (simplified parsing)
        table = None
        if 'FROM EVENT_TYPE' in self.last_query:
            table = 'event_type'
        elif 'FROM EVENTS' in self.last_query:
            table = 'events'
        elif 'FROM PARTICIPANTS' in self.last_query:
            table = 'participants'
        
        if table and table in MOCK_DATA:
            # Filter by params if needed (simplified)
            if params and 'WHERE' in self.last_query:
                # Very basic filtering - just for testing purposes
                if table == 'event_type' and 'TYPE_ID = %s' in self.last_query:
                    self.results = [row for row in MOCK_DATA[table] if row[0] == params[0]]
                else:
                    # Default to returning all data for the table
                    self.results = MOCK_DATA[table]
            else:
                self.results = MOCK_DATA[table]
        else:
            self.results = []
    
    def _handle_insert(self, query, params):
        # For testing, we'll just simulate successful insert
        pass
    
    def _handle_delete(self, query, params):
        # For testing, we'll just simulate successful delete
        pass
        
    def fetchall(self):
        return self.results
        
    def fetchone(self):
        return self.results[0] if self.results else None
        
    def close(self):
        pass

# Mock connection pool instance
connection_pool = MockConnectionPool()

def initialize_connection_pool():
    """Mock initialization that always succeeds"""
    return True

def get_db_connection():
    """Get a mock database connection"""
    return MockConnection()

def run_query(query, params=None):
    """Execute a query against mock data and return results"""
    connection = None
    cursor = None
    results = []
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        cursor.execute(query, params)
        
        # Try to fetch results if it's a SELECT query
        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
        else:
            # For non-SELECT queries, just return True to indicate success
            results = True
            
    except Exception as e:
        print(f"Mock DB Error: {e}")
        # Return empty list for SELECT or False for other queries
        results = [] if query.strip().upper().startswith('SELECT') else False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
    return results