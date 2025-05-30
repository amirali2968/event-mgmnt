import sys
import time
import os
from database.db_connection import get_db_connection, run_query, connection_pool

def test_connection():
    """Test database connection"""
    print("\n1. Testing database connection...")
    connection = get_db_connection()
    if connection and connection.is_connected():
        print("✓ Connection successful!")
        connection.close()
        return True
    else:
        print("✗ Connection failed!")
        return False

def test_select_query():
    """Test SELECT query functionality"""
    print("\n2. Testing SELECT query...")
    # Try to get event types from the database
    query = "SELECT * FROM event_type LIMIT 5"
    results = run_query(query)
    
    if results:
        print(f"✓ SELECT query successful! Found {len(results)} results:")
        for i, row in enumerate(results[:3], 1):  # Show up to 3 results
            print(f"  Result {i}: {row}")
        if len(results) > 3:
            print(f"  ... and {len(results) - 3} more")
        return True
    else:
        print("✗ SELECT query failed or returned no results")
        return False

def test_transaction():
    """Test transaction functionality with INSERT and DELETE"""
    print("\n3. Testing transaction functionality...")
    
    # Create a temporary test record
    test_id = int(time.time())  # Use timestamp as unique ID
    insert_query = "INSERT INTO event_type (type_id, type_name, description) VALUES (%s, %s, %s)"
    insert_params = (test_id, "TEST_EVENT_TYPE", "Temporary test record")
    
    # Insert the test record
    insert_result = run_query(insert_query, insert_params)
    if not insert_result:
        print("✗ INSERT query failed")
        return False
    
    # Verify the record was inserted
    verify_query = "SELECT * FROM event_type WHERE type_id = %s"
    verify_params = (test_id,)
    verify_result = run_query(verify_query, verify_params)
    
    if not verify_result or len(verify_result) == 0:
        print("✗ Failed to verify inserted record")
        return False
    
    print(f"✓ INSERT query successful! Added test record with ID {test_id}")
    
    # Clean up by deleting the test record
    delete_query = "DELETE FROM event_type WHERE type_id = %s"
    delete_params = (test_id,)
    delete_result = run_query(delete_query, delete_params)
    
    if not delete_result:
        print(f"✗ DELETE query failed for test record {test_id}")
        return False
    
    # Verify the record was deleted
    verify_delete = run_query(verify_query, verify_params)
    if verify_delete and len(verify_delete) > 0:
        print(f"✗ Failed to delete test record {test_id}")
        return False
    
    print(f"✓ DELETE query successful! Removed test record with ID {test_id}")
    return True

def test_error_handling():
    """Test error handling with an invalid query"""
    print("\n4. Testing error handling...")
    
    # Run an invalid query
    invalid_query = "SELECT * FROM non_existent_table"
    results = run_query(invalid_query)
    
    # Should return an empty list, not crash
    if results == []:
        print("✓ Error handling successful! Invalid query handled gracefully")
        return True
    else:
        print("✗ Error handling failed")
        return False

def check_mysql_server():
    """Check if MySQL server is running and accessible"""
    print("\n=== MySQL Server Check ===")
    print(f"Checking connection to MySQL server at: {os.environ.get('DB_HOST', 'localhost')}")
    
    if connection_pool is None:
        print("❌ Connection pool initialization failed. Please check if MySQL server is running.")
        print("\nTroubleshooting tips:")
        print("1. Make sure MySQL server is installed and running")
        print("2. Verify database credentials in config.py")
        print("3. Check if the database 'event_mgmt' exists")
        print("4. Ensure network connectivity to the database server")
        return False
    return True

def main():
    print("=== Database Connection Module Test ===\n")
    
    # First check if MySQL server is accessible
    if not check_mysql_server():
        return 1
    
    # Run all tests
    tests = [
        test_connection,
        test_select_query,
        test_transaction,
        test_error_handling
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    # Summary
    print("\n=== Test Summary ===")
    passed = results.count(True)
    failed = results.count(False)
    print(f"Passed: {passed}/{len(results)}")
    print(f"Failed: {failed}/{len(results)}")
    
    if failed == 0:
        print("\n✅ All tests passed! The database connection module is working properly.")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the database connection module.")
        return 1

if __name__ == "__main__":
    sys.exit(main())