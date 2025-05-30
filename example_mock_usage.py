"""Example script demonstrating how to use the mock database connection.

This script shows how to use the database utility functions to switch between
real and mock database connections and perform basic operations.
"""

# Import the database utility functions
from database.db_utils import execute_query, set_mock_mode

def display_event_types():
    """Display all event types from the database"""
    print("\nFetching event types...")
    query = "SELECT * FROM event_type"
    results = execute_query(query)
    
    if results:
        print(f"Found {len(results)} event types:")
        for row in results:
            print(f"  - {row[1]}: {row[2]}")
    else:
        print("No event types found or query failed")

def display_events():
    """Display all events from the database"""
    print("\nFetching events...")
    query = "SELECT * FROM events"
    results = execute_query(query)
    
    if results:
        print(f"Found {len(results)} events:")
        for row in results:
            print(f"  - {row[1]} (from {row[2]} to {row[3]})")
    else:
        print("No events found or query failed")

def main():
    print("=== Event Management System - Mock Database Example ===\n")
    
    # Ensure we're using the mock database
    current_module = set_mock_mode(True)
    print(f"Using database module: {current_module}")
    
    # Display data from the mock database
    display_event_types()
    display_events()
    
    print("\n=== Example Complete ===")
    print("Note: To use a real database connection, call set_mock_mode(False)")
    print("      or set the USE_MOCK_DB environment variable to 'False'")

if __name__ == "__main__":
    main()