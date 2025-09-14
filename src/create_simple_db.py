#!/usr/bin/env python3
"""
Simple database creation script for Windows
"""

import sqlite3
import os
import sys

def create_simple_database():
    """Create a simple database with sample data."""
    
    print("[INFO] Creating simple database...")
    
    # Database file path
    db_path = "finbin_farm_data.db"
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"[INFO] Removed existing database: {db_path}")
    
    try:
        # Create database connection
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("[INFO] Creating database schema...")
        
        # Create hdb_main_data table
        cursor.execute("""
            CREATE TABLE hdb_main_data (
                hdb_main_data_id TEXT PRIMARY KEY,
                file_id TEXT,
                tenant_id TEXT,
                organization_id TEXT,
                branch_id TEXT,
                branch_state TEXT,
                primary_banker_user_id TEXT,
                primary_banker_name TEXT,
                analyst_name TEXT,
                fbm_farm_id TEXT,
                finbin_id TEXT,
                finbin_id_year TEXT,
                dataset TEXT,
                fp_source_id TEXT,
                fp_source_date_modified TEXT,
                analysis_type TEXT,
                year TEXT,
                state TEXT,
                county TEXT,
                client_first_last_name TEXT,
                client_addr_city_state TEXT,
                delete_data TEXT
            )
        """)
        print("[OK] Created hdb_main_data table")
        
        # Create fm_genin table
        cursor.execute("""
            CREATE TABLE fm_genin (
                fm_genin_guid TEXT PRIMARY KEY,
                hdb_main_data_id TEXT,
                item_name TEXT
            )
        """)
        print("[OK] Created fm_genin table")
        
        # Create fm_guide table (simplified)
        cursor.execute("""
            CREATE TABLE fm_guide (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                current_ratio_beg REAL,
                current_ratio_end REAL,
                net_farm_income_cost REAL,
                net_farm_income_mkt REAL
            )
        """)
        print("[OK] Created fm_guide table")
        
        # Create other tables
        other_tables = [
            'fm_stmts', 'fm_prf_lq', 'fm_cap_ad', 'fm_hhold', 
            'fm_nf_ie', 'fm_fm_exp', 'fm_fm_inc', 'fm_beg_bs_end_bs'
        ]
        
        for table_name in other_tables:
            cursor.execute(f"""
                CREATE TABLE {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item_name TEXT,
                    fm_genin_guid TEXT,
                    hdb_main_data_id TEXT
                )
            """)
            print(f"[OK] Created {table_name} table")
        
        print("[INFO] Inserting sample data...")
        
        # Insert sample data to hdb_main_data
        cursor.execute("""
            INSERT INTO hdb_main_data (
                hdb_main_data_id, file_id, tenant_id, organization_id, 
                branch_id, branch_state, primary_banker_user_id, primary_banker_name, 
                analyst_name, fbm_farm_id, finbin_id, finbin_id_year, dataset, 
                fp_source_id, fp_source_date_modified, analysis_type, year, 
                state, county, client_first_last_name, client_addr_city_state, delete_data
            ) VALUES 
            ('farm_001', 'file_001', 'tenant_001', 'org_001', 
             'branch_001', 'MN', 'banker_001', 'John Smith', 'Analyst A', 
             'farm_001', 'finbin_001', '2021', 'dataset_001', 'source_001', 
             '2023-01-15', 'analysis_001', '2021', 'MN', 'Hennepin', 
             'Johnson Dairy Farm', 'Minneapolis, MN', 'N'),
            ('farm_002', 'file_002', 'tenant_002', 'org_002', 
             'branch_002', 'WI', 'banker_002', 'Jane Doe', 'Analyst B', 
             'farm_002', 'finbin_002', '2021', 'dataset_002', 'source_002', 
             '2023-02-20', 'analysis_002', '2021', 'WI', 'Dane', 
             'Green Valley Corn Farm', 'Madison, WI', 'N'),
            ('farm_003', 'file_003', 'tenant_003', 'org_003', 
             'branch_003', 'ND', 'banker_003', 'Bob Johnson', 'Analyst C', 
             'farm_003', 'finbin_003', '2021', 'dataset_003', 'source_003', 
             '2023-03-10', 'analysis_003', '2021', 'ND', 'Cass', 
             'Prairie Wheat Farm', 'Fargo, ND', 'N')
        """)
        print("[OK] Added 3 farms to hdb_main_data")
        
        # Insert sample data to fm_genin
        cursor.execute("""
            INSERT INTO fm_genin (
                fm_genin_guid, hdb_main_data_id, item_name
            ) VALUES 
            ('guid_001', 'farm_001', 'Johnson Dairy Farm'),
            ('guid_002', 'farm_002', 'Green Valley Corn Farm'),
            ('guid_003', 'farm_003', 'Prairie Wheat Farm')
        """)
        print("[OK] Added 3 records to fm_genin")
        
        # Insert sample data to fm_guide
        cursor.execute("""
            INSERT INTO fm_guide (
                item_name, fm_genin_guid, hdb_main_data_id, 
                current_ratio_beg, current_ratio_end, 
                net_farm_income_cost, net_farm_income_mkt
            ) VALUES 
            ('Johnson Dairy Farm', 'guid_001', 'farm_001', 2.1, 2.3, 185000.00, 185000.00),
            ('Green Valley Corn Farm', 'guid_002', 'farm_002', 2.8, 3.1, 320000.00, 320000.00),
            ('Prairie Wheat Farm', 'guid_003', 'farm_003', 2.4, 2.7, 275000.00, 275000.00)
        """)
        print("[OK] Added 3 records to fm_guide")
        
        # Insert sample data to other tables
        for table_name in other_tables:
            cursor.execute(f"""
                INSERT INTO {table_name} (
                    item_name, fm_genin_guid, hdb_main_data_id
                ) VALUES 
                ('Sample Data - Farm 1', 'guid_001', 'farm_001'),
                ('Sample Data - Farm 2', 'guid_002', 'farm_002'),
                ('Sample Data - Farm 3', 'guid_003', 'farm_003')
            """)
            print(f"[OK] Added 3 records to {table_name}")
        
        # Commit changes
        conn.commit()
        conn.close()
        
        print("[SUCCESS] Database created successfully!")
        print(f"[INFO] Database file: {db_path}")
        
        # Verify the database
        verify_database(db_path)
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Database creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_database(db_path):
    """Verify the database has data."""
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
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
        
        print(f"[INFO] Total rows across all tables: {total_rows}")
        
        if total_rows > 0:
            print("[SUCCESS] Database has data!")
        else:
            print("[ERROR] Database is empty!")
            
        conn.close()
        
    except Exception as e:
        print(f"[ERROR] Error checking database: {e}")

if __name__ == "__main__":
    success = create_simple_database()
    sys.exit(0 if success else 1)
