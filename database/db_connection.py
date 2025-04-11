import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """
    Establish and return a connection to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='event_mgmt',
            user='root',
            password='root'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def run_query(query, fetch_results=True):
    """
    Execute a query on the database.
    
    Args:
        query (str): The SQL query to execute.
        fetch_results (bool): Whether to fetch and return results (default: True).
    
    Returns:
        list: Query results if fetch_results is True, otherwise an empty list.
    """
    connection = get_db_connection()
    if not connection:
        return []

    try:
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        connection.commit()

        if fetch_results:
            try:
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(f"No results to fetch: {e}")
                return []

    except Error as e:
        print(f"Error executing query: {e}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

    return []