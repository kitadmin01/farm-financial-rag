#!/usr/bin/env python3
"""
Test script to verify database creation works
"""

import os
import sys
import sqlite3

def test_database_creation():
    """Test database creation and data insertion."""
    
    print("🧪 Testing Database Creation")
    print("=" * 40)
    
    # Change to src directory
    os.chdir("src")
    
    # Remove existing database
    if os.path.exists("finbin_farm_data.db"):
        os.remove("finbin_farm_data.db")
        print("🗑️  Removed existing database")
    
    # Import and run create_database
    try:
        import create_database
        create_database.main()
        print("\n✅ Database creation completed")
        
        # Check database contents
        conn = sqlite3.connect("finbin_farm_data.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        total_rows = 0
        for table in tables:
            table_name = table[0]
            if table_name != 'sqlite_sequence':
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                total_rows += count
                print(f"  {table_name}: {count} rows")
        
        print(f"\n📊 Total rows: {total_rows}")
        
        if total_rows > 0:
            print("✅ SUCCESS: Database has data!")
        else:
            print("❌ FAILED: Database is empty!")
            
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_database_creation()
