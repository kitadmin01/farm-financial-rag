#!/usr/bin/env python3
"""
Test script to verify database creation works
"""

import sqlite3
import os
import sys

def test_database_creation():
    """Test database creation and data insertion."""
    
    print("[TEST] Testing database creation...")
    
    # Remove existing database if it exists
    db_path = "finbin_farm_data.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"[INFO] Removed existing database: {db_path}")
    
    try:
        # Create database connection
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("[TEST] Creating database schema...")
        
        # Create a simple test table
        cursor.execute("""
            CREATE TABLE test_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                value REAL
            )
        """)
        
        # Insert test data
        cursor.execute("""
            INSERT INTO test_table (name, value) VALUES 
            ('Test 1', 100.5),
            ('Test 2', 200.7),
            ('Test 3', 300.9)
        """)
        
        # Commit changes
        conn.commit()
        
        # Verify data
        cursor.execute("SELECT COUNT(*) FROM test_table")
        count = cursor.fetchone()[0]
        
        print(f"[INFO] Inserted {count} test records")
        
        # Close connection
        conn.close()
        
        if count == 3:
            print("[SUCCESS] Database creation test passed!")
            return True
        else:
            print(f"[ERROR] Expected 3 records, got {count}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Database creation test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_database_creation()
    sys.exit(0 if success else 1)