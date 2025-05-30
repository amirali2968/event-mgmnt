"""Utility functions for database connection management.

This module provides helper functions to easily switch between real and mock
database connections based on configuration or environment variables.
"""

import os
import importlib

# Default to mock mode if no real database is available
USE_MOCK_DB = os.environ.get('USE_MOCK_DB', 'True').lower() in ('true', '1', 't')

def get_db_module():
    """Get the appropriate database module based on configuration.
    
    Returns:
        module: Either the real or mock database connection module
    """
    if USE_MOCK_DB:
        print("Using MOCK database connection for testing")
        return importlib.import_module('database.mock_db_connection')
    else:
        print("Using REAL database connection")
        return importlib.import_module('database.db_connection')

def get_connection():
    """Get a database connection (real or mock).
    
    Returns:
        connection: A database connection object
    """
    db_module = get_db_module()
    return db_module.get_db_connection()

def execute_query(query, params=None):
    """Execute a query using the appropriate database module.
    
    Args:
        query (str): SQL query to execute
        params (tuple, optional): Parameters for the query
        
    Returns:
        list: Query results or empty list on error
    """
    db_module = get_db_module()
    return db_module.run_query(query, params)

def set_mock_mode(use_mock=True):
    """Set whether to use mock database or real database.
    
    Args:
        use_mock (bool): Whether to use mock database
    """
    global USE_MOCK_DB
    USE_MOCK_DB = use_mock
    os.environ['USE_MOCK_DB'] = str(use_mock)
    
    # Return the current module being used for confirmation
    return get_db_module().__name__