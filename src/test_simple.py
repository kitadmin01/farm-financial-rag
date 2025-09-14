#!/usr/bin/env python3
"""
Simple test to verify database creation works
"""

import sqlite3
import os

def test_simple_db():
    """Test simple database creation."""
    
    print("Testing simple database creation...")
    
    # Remove existing database
    db_path = "finbin_farm_data.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Removed existing database")
    
    try:
        # Create database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create simple table
        cursor.execute("""
            CREATE TABLE test_table (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)
        
        # Insert data
        cursor.execute("INSERT INTO test_table (name) VALUES ('test1'), ('test2'), ('test3')")
        
        # Commit
        conn.commit()
        conn.close()
        
        # Verify
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM test_table")
        count = cursor.fetchone()[0]
        conn.close()
        
        print(f"Database created successfully with {count} rows")
        return count == 3
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = test_simple_db()
    print("SUCCESS" if success else "FAILED")
