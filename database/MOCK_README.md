# Mock Database Connection Module

This module provides a simulated database connection for testing the Event Management System without requiring a real MySQL database.

## Overview

The mock database connection module (`mock_db_connection.py`) provides:

- Simulated database connections that always succeed
- Pre-populated mock data for testing
- Query execution that returns appropriate test data
- Simulated transaction handling
- Error handling similar to the real module

## Why Use Mock Database?

- **Development without Database**: Allows developers to work on application logic without setting up a database
- **Consistent Testing**: Provides consistent test data regardless of database state
- **CI/CD Friendly**: Enables running tests in environments where database access is limited
- **Faster Testing**: Eliminates database connection overhead during testing

## Usage

To use the mock database connection instead of the real one, simply import from the mock module:

```python
# Instead of:
# from database.db_connection import run_query

# Use:
from database.mock_db_connection import run_query
```

## Testing the Mock Connection

Run the mock test script to verify the mock database functionality:

```bash
python test_mock_db_connection.py
```

The test script will:
1. Test mock connection functionality
2. Test SELECT query execution against mock data
3. Test simulated transaction handling (INSERT/DELETE)
4. Test error handling

## Mock Data

The mock module contains pre-populated data for:

- `event_type`: Different types of events
- `events`: Sample event records
- `participants`: Sample participant records

You can modify the mock data in `mock_db_connection.py` to suit your testing needs.

## Limitations

- Limited SQL parsing (only handles basic queries)
- No complex JOIN operations
- No actual data persistence between runs
- Simplified transaction handling

## Switching Between Real and Mock

For production code, always use the real database connection module. The mock module is intended for testing and development purposes only.