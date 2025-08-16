#!/usr/bin/env python3
"""
Script to check the actual table schema in the existing database.
"""

import sqlite3
import os

def check_table_schema():
    """Check the actual schema of all tables in the database."""
    
    db_path = "finbin_farm_data.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("📊 Checking Database Table Schemas")
        print("=" * 60)
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            print(f"\n🔍 Table: {table_name}")
            print("-" * 40)
            
            try:
                # Get table schema
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = cursor.fetchall()
                
                if columns:
                    print(f"Columns ({len(columns)}):")
                    for col in columns:
                        col_id, col_name, col_type, not_null, default_val, pk = col
                        pk_marker = " (PRIMARY KEY)" if pk else ""
                        not_null_marker = " NOT NULL" if not_null else ""
                        print(f"  {col_id}: {col_name} ({col_type}){not_null_marker}{pk_marker}")
                else:
                    print("No columns found")
                    
                # Get row count
                cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
                count = cursor.fetchone()[0]
                print(f"Row count: {count}")
                
            except Exception as e:
                print(f"Error checking table {table_name}: {e}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")

if __name__ == "__main__":
    check_table_schema()
