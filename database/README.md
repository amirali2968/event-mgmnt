# Database Connection Module

This module provides a connection pool and query execution functionality for the Event Management System.

## Overview

The database connection module (`db_connection.py`) provides:

- Connection pooling for efficient database access
- Retry logic for connection failures
- Query execution with parameter support
- Transaction management
- Error handling

## Setup Requirements

1. **MySQL Server**: Ensure MySQL server is installed and running
2. **Database**: Create a database named `event_mgmt` (or as configured)
3. **Environment Variables**: Set the following environment variables or update `config.py`:
   - `DB_HOST`: Database host (default: localhost)
   - `DB_NAME`: Database name (default: event_mgmt)
   - `DB_USER`: Database username (default: root)
   - `DB_PASSWORD`: Database password (default: root)
   - `FLASK_ENV`: Environment (development, testing, production)

## Testing the Connection

Run the test script to verify the database connection:

```bash
python test_db_connection.py
```

The test script will:
1. Check if MySQL server is accessible
2. Test basic connection functionality
3. Test SELECT query execution
4. Test transaction handling (INSERT/DELETE)
5. Test error handling

## Troubleshooting

If you encounter connection issues:

1. **MySQL Server**: Ensure MySQL server is running
   ```bash
   # Windows
   net start mysql
   
   # Linux
   sudo systemctl status mysql
   ```

2. **Database Existence**: Verify the database exists
   ```sql
   CREATE DATABASE IF NOT EXISTS event_mgmt;
   ```

3. **Credentials**: Check username and password in `config.py`

4. **Firewall**: Ensure port 3306 is open if connecting to a remote server

5. **Connection Timeout**: Increase the connection timeout in `db_connection.py` if needed

## Usage Examples

```python
from database.db_connection import run_query

# SELECT query
results = run_query("SELECT * FROM events LIMIT 10")
for row in results:
    print(row)

# INSERT with parameters
run_query(
    "INSERT INTO participants (event_id, fullname, email) VALUES (%s, %s, %s)", 
    (1, "John Doe", "john@example.com")
)
```