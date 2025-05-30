import mysql.connector
from mysql.connector import Error, pooling
import sys
import time
from config import get_config

# Get configuration
config = get_config()

# Create a connection pool
connection_pool = None

# Maximum number of connection attempts
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds

def initialize_connection_pool():
    """Initialize the connection pool with retry logic"""
    global connection_pool
    
    for attempt in range(MAX_RETRIES):
        try:
            connection_pool = pooling.MySQLConnectionPool(
                pool_name="event_mgmt_pool",
                pool_size=5,
                host=config.DB_HOST,
                database=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                connection_timeout=10
            )
            # Test the connection
            conn = connection_pool.get_connection()
            if conn.is_connected():
                conn.close()
                print(f"Connection pool created successfully on attempt {attempt+1}")
                return True
        except Error as e:
            print(f"Attempt {attempt+1}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                print(f"Retrying in {RETRY_DELAY} seconds...")
                time.sleep(RETRY_DELAY)
            else:
                print("All connection attempts failed. Please check your MySQL server and configuration.")
                print(f"Connection details: host={config.DB_HOST}, database={config.DB_NAME}, user={config.DB_USER}")
                return False
    return False

# Initialize the connection pool
initialize_connection_pool()

def get_db_connection():
    """
    Get a connection from the pool.
    """
    if connection_pool is None:
        print("Error: Connection pool is not initialized")
        return None
        
    try:
        connection = connection_pool.get_connection()
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    return None

def run_query(query, params=None):
    """
    Execute a query and return the results.
    
    Args:
        query (str): SQL query to execute
        params (tuple, optional): Parameters for the query
        
    Returns:
        list: Query results or empty list on error
    """
    connection = None
    cursor = None
    results = []
    
    try:
        connection = get_db_connection()
        if connection is None:
            return results
            
        cursor = connection.cursor(buffered=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        # Try to fetch results if it's a SELECT query
        if query.strip().upper().startswith('SELECT'):
            results = cursor.fetchall()
        else:
            connection.commit()
            results = True
            
    except Error as e:
        print(f"Error executing query: {e}")
        if connection:
            connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            
    return results