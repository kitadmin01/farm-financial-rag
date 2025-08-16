#!/usr/bin/env python3
"""
Minimal Script to add basic sample data to the database tables.
Only inserts into tables with simple schemas to avoid column count issues.
"""

import sqlite3
import os

def add_sample_data():
    """Add basic sample data to tables with simple schemas."""
    
    db_path = "finbin_farm_data.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("📊 Adding sample data to database...")
        print("=" * 50)
        
        # Add sample data to hdb_main_data (22 columns - confirmed working)
        print("Adding data to hdb_main_data...")
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
             'Sample Farm 1', 'Minneapolis, MN', 'N'),
            ('farm_002', 'file_002', 'tenant_002', 'org_002', 
             'branch_002', 'WI', 'banker_002', 'Jane Doe', 'Analyst B', 
             'farm_002', 'finbin_002', '2021', 'dataset_002', 'source_002', 
             '2023-02-20', 'analysis_002', '2021', 'WI', 'Dane', 
             'Sample Farm 2', 'Madison, WI', 'N'),
            ('farm_003', 'file_003', 'tenant_003', 'org_003', 
             'branch_003', 'ND', 'banker_003', 'Bob Johnson', 'Analyst C', 
             'farm_003', 'finbin_003', '2021', 'dataset_003', 'source_003', 
             '2023-03-10', 'analysis_003', '2021', 'ND', 'Cass', 
             'Sample Farm 3', 'Fargo, ND', 'N')
        """)
        print("✅ Added 3 farms to hdb_main_data")
        
        # Add sample data to fm_genin (3 columns - confirmed working)
        print("Adding data to fm_genin...")
        cursor.execute("""
            INSERT INTO fm_genin (
                fm_genin_guid, hdb_main_data_id, item_name
            ) VALUES 
            ('guid_001', 'farm_001', 'Sample Farm 1'),
            ('guid_002', 'farm_002', 'Sample Farm 2'),
            ('guid_003', 'farm_003', 'Sample Farm 3')
        """)
        print("✅ Added 3 records to fm_genin")
        
        # Add sample data to fm_guide (only first 3 columns to avoid column count issues)
        print("Adding data to fm_guide...")
        cursor.execute("""
            INSERT INTO fm_guide (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Sample Farm 1', 'guid_001', 'farm_001'),
            ('Sample Farm 2', 'guid_002', 'farm_002'),
            ('Sample Farm 3', 'guid_003', 'farm_003')
        """)
        print("✅ Added 3 records to fm_guide")
        
        # Add sample data to fm_stmts (only first 3 columns to avoid column count issues)
        print("Adding data to fm_stmts...")
        cursor.execute("""
            INSERT INTO fm_stmts (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Sample Farm 1', 'guid_001', 'farm_001'),
            ('Sample Farm 2', 'guid_002', 'farm_002'),
            ('Sample Farm 3', 'guid_003', 'farm_003')
        """)
        print("✅ Added 3 records to fm_stmts")
        
        # Add sample data to other tables (all have simple 4-column schemas)
        tables_to_populate = ['fm_prf_lq', 'fm_cap_ad', 'fm_hhold', 'fm_nf_ie', 'fm_fm_exp', 'fm_fm_inc', 'fm_beg_bs_end_bs']
        
        for table in tables_to_populate:
            print(f"Adding data to {table}...")
            cursor.execute(f"""
                INSERT INTO {table} (
                    item_name, fm_genin_guid, hdb_main_data_id
                ) VALUES 
                ('Sample Farm 1', 'guid_001', 'farm_001'),
                ('Sample Farm 2', 'guid_002', 'farm_002'),
                ('Sample Farm 3', 'guid_003', 'farm_003')
            """)
            print(f"✅ Added 3 records to {table}")
        
        # Commit all changes
        conn.commit()
        conn.close()
        
        print("\n" + "=" * 50)
        print("🎉 Sample data added successfully!")
        print("Database now contains sample farm data for testing.")
        
    except Exception as e:
        print(f"❌ Error adding sample data: {e}")
        if 'conn' in locals():
            conn.close()

def check_data():
    """Check the data in the database."""
    
    db_path = "finbin_farm_data.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("📊 Checking database contents...")
        print("=" * 50)
        
        # Check all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        total_rows = 0
        
        for table in tables:
            table_name = table[0]
            if table_name == 'sqlite_sequence':  # Skip system table
                continue
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
        
        if total_rows > 0:
            print("✅ Database has data!")
        else:
            print("❌ Database is still empty")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error checking data: {e}")

def main():
    """Main function."""
    print("🌾 Adding Sample Data to Farm Financial Database (Minimal Version)")
    print("=" * 70)
    
    # Add sample data
    add_sample_data()
    
    print("\n" + "=" * 70)
    
    # Check the data
    check_data()

if __name__ == "__main__":
    main()
