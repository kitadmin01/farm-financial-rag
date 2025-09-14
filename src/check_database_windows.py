#!/usr/bin/env python3
"""
Windows-compatible script to check database contents (no emoji characters)
"""

import sqlite3
import os
import sys

def check_database():
    """Check database contents."""
    db_path = "finbin_farm_data.db"
    
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file not found: {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        print(f"[INFO] Database: {db_path}")
        print(f"[INFO] Found {len(tables)} tables:")
        print("=" * 50)
        
        total_rows = 0
        
        for table in tables:
            table_name = table[0]
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                total_rows += count
                status = "[OK]" if count > 0 else "[EMPTY]"
                print(f"{status} {table_name}: {count} rows")
            except Exception as e:
                print(f"[ERROR] {table_name}: Error - {e}")
        
        print("=" * 50)
        print(f"[INFO] Total rows across all tables: {total_rows}")
        
        # Check if data exists
        if total_rows == 0:
            print("\n[WARNING] All tables are empty!")
            print("   The database creation script may not have completed successfully.")
            print("   Run: python create_database.py")
            return False
        else:
            print(f"\n[SUCCESS] Database has {total_rows} rows of data")
            return True
        
        conn.close()
        
    except Exception as e:
        print(f"[ERROR] Database error: {e}")
        return False

if __name__ == "__main__":
    success = check_database()
    sys.exit(0 if success else 1)
