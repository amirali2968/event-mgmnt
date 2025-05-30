"""Database package initialization.

This module provides a convenient way to import database functions
without having to specify whether to use the real or mock implementation.
"""

# Import the utility functions that handle switching between real and mock
from database.db_utils import execute_query, get_connection, set_mock_mode

# For backward compatibility, provide the run_query function
# that routes can continue to use without changing their imports
def run_query(query, params=None):
    """Execute a query using either real or mock database connection.
    
    This function maintains backward compatibility with existing code
    that imports run_query from database.db_connection.
    
    Args:
        query (str): SQL query to execute
        params (tuple, optional): Parameters for the query
        
    Returns:
        list: Query results or empty list on error
    """
    return execute_query(query, params)

# By default, use mock database if no real database is available
# This can be overridden by setting the USE_MOCK_DB environment variable