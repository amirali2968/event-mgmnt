import sys
import time
import os

# Import the mock database connection module instead of the real one
from database.mock_db_connection import get_db_connection, run_query, connection_pool

def test_connection():
    """Test mock database connection"""
    print("\n1. Testing mock database connection...")
    connection = get_db_connection()
    if connection and connection.is_connected():
        print("✓ Mock connection successful!")
        connection.close()
        return True
    else:
        print("✗ Mock connection failed!")
        return False

def test_select_query():
    """Test SELECT query functionality with mock data"""
    print("\n2. Testing SELECT query with mock data...")
    # Try to get event types from the mock database
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
    """Test transaction functionality with INSERT and DELETE using mock data"""
    print("\n3. Testing transaction functionality with mock data...")
    
    # Create a temporary test record
    test_id = int(time.time())  # Use timestamp as unique ID
    insert_query = "INSERT INTO event_type (type_id, type_name, description) VALUES (%s, %s, %s)"
    insert_params = (test_id, "TEST_EVENT_TYPE", "Temporary test record")
    
    # Insert the test record
    insert_result = run_query(insert_query, insert_params)
    if not insert_result:
        print("✗ INSERT query failed")
        return False
    
    print(f"✓ INSERT query simulation successful! (Mock data not actually modified)")
    
    # Clean up by deleting the test record
    delete_query = "DELETE FROM event_type WHERE type_id = %s"
    delete_params = (test_id,)
    delete_result = run_query(delete_query, delete_params)
    
    if not delete_result:
        print(f"✗ DELETE query failed for test record {test_id}")
        return False
    
    print(f"✓ DELETE query simulation successful! (Mock data not actually modified)")
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

def main():
    print("=== Mock Database Connection Module Test ===\n")
    print("NOTE: This test uses mock data and does not require a real database connection.")
    print("      All database operations are simulated for testing purposes.")
    
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
        print("\n✅ All tests passed! The mock database connection module is working properly.")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the mock database connection module.")
        return 1

if __name__ == "__main__":
    sys.exit(main())