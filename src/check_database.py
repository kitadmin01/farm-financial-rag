#!/usr/bin/env python3
"""
Simple script to check database contents
"""

import sqlite3
import os

def check_database():
    """Check database contents."""
    db_path = "finbin_farm_data.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"📊 Database: {db_path}")
        print(f"📋 Found {len(tables)} tables:")
        print("=" * 50)
        
        total_rows = 0
        
        for table in tables:
            table_name = table[0]
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                total_rows += count
                status = "✅" if count > 0 else "❌"
                print(f"{status} {table_name}: {count} rows")
            except Exception as e:
                print(f"❌ {table_name}: Error - {e}")
        
        print("=" * 50)
        print(f"📈 Total rows across all tables: {total_rows}")
        
        # Check if data exists
        if total_rows == 0:
            print("\n⚠️  WARNING: All tables are empty!")
            print("   The database creation script may not have completed successfully.")
            print("   Run: python create_database.py")
        else:
            print(f"\n✅ Database has {total_rows} rows of data")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    check_database()
