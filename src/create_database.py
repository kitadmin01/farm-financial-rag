#!/usr/bin/env python3
"""
Script to create the SQLite database schema and insert data from CSV files.
This is the essential script for first-time database setup.
"""

import sqlite3
import pandas as pd
import os
from pathlib import Path

def create_database_schema(cursor):
    """Create all database tables with proper schemas."""
    
    # Drop existing tables if they exist
    tables_to_drop = [
        'hdb_main_data', 'fm_genin', 'fm_guide', 'fm_stmts', 
        'fm_prf_lq', 'fm_cap_ad', 'fm_hhold', 'fm_nf_ie', 
        'fm_fm_exp', 'fm_fm_inc', 'fm_beg_bs_end_bs'
    ]
    
    for table in tables_to_drop:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
    
    # Create tables with proper schemas
    schemas = {
        'hdb_main_data': '''
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
        ''',
        
        'fm_genin': '''
            CREATE TABLE fm_genin (
                fm_genin_guid TEXT PRIMARY KEY,
                hdb_main_data_id TEXT,
                item_name TEXT,
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_guide': '''
            CREATE TABLE fm_guide (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                current_ratio_beg REAL,
                current_ratio_end REAL,
                working_capital_beg REAL,
                working_capital_end REAL,
                working_cap_to_rev_beg TEXT,
                working_cap_to_rev_end TEXT,
                rate_of_ret_on_farm_assets_cost REAL,
                rate_of_ret_on_farm_assets_mkt REAL,
                rate_of_ret_on_farm_equity_cost REAL,
                rate_of_ret_on_farm_equity_mkt REAL,
                operating_profit_margin_cost REAL,
                operating_profit_margin_mkt REAL,
                net_farm_income_cost REAL,
                net_farm_income_mkt REAL,
                ebitda_cost REAL,
                ebitda_mkt REAL,
                capital_repayment_capacity TEXT,
                capital_repayment_margin REAL,
                term_debt_coverage_ratio_accr REAL,
                replacement_margin REAL,
                repl_margin_coverage_ratio REAL,
                asset_turnover_rate_cost REAL,
                asset_turnover_rate_mkt REAL,
                operating_expense_ratio REAL,
                interest_expense_ratio REAL,
                depreciation_expense_ratio REAL,
                net_farm_income_ratio REAL,
                beg_cost_farm_debt_to_asset_ratio REAL,
                end_cost_farm_debt_to_asset_ratio REAL,
                beg_mkt_farm_debt_to_asset_ratio REAL,
                end_mkt_farm_debt_to_asset_ratio REAL,
                beg_mkt_fm_debt_to_asset_ratio_no_def REAL,
                end_mkt_fm_debt_to_asset_ratio_no_def REAL,
                beg_cost_farm_equity_to_asset_ratio REAL,
                end_cost_farm_equity_to_asset_ratio REAL,
                beg_mkt_farm_equity_to_asset_ratio REAL,
                end_mkt_farm_equity_to_asset_ratio REAL,
                beg_mkt_fm_equity_to_asset_ratio_no_def REAL,
                end_mkt_fm_equity_to_asset_ratio_no_def REAL,
                beg_cost_farm_debt_to_equity_ratio REAL,
                end_cost_farm_debt_to_equity_ratio REAL,
                beg_mkt_farm_debt_to_equity_ratio REAL,
                end_mkt_farm_debt_to_equity_ratio REAL,
                beg_mkt_fm_debt_to_equity_ratio_no_def REAL,
                end_mkt_fm_debt_to_equity_ratio_no_def REAL,
                term_debt_to_ebitda REAL,
                working_cap_to_exp_beg REAL,
                working_cap_to_exp_end REAL,
                debt_coverage_ratio_accr REAL,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_stmts': '''
            CREATE TABLE fm_stmts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                beginning_net_worth REAL,
                net_farm_income REAL,
                change_in_nonfarm_assets REAL,
                change_in_nonfarm_accts_payable REAL,
                other_cash_flows REAL,
                total_change_in_retained_earnings TEXT,
                debts_forgiven REAL,
                capital_loss_on_repossessions REAL,
                total_change_in_contributed_cap TEXT,
                change_in_mkt_value_of_cap_assets TEXT,
                change_in_deferred_liabilities REAL,
                total_change_in_market_value REAL,
                total_change_in_net_worth REAL,
                ending_net_worth_calculated REAL,
                ending_net_worth_reported REAL,
                equity_discrepancy REAL,
                beg_cash_balance_farm_and_nonfarm REAL,
                gross_cash_farm_income REAL,
                total_cash_farm_expense REAL,
                net_cash_from_hedging REAL,
                cash_from_operations REAL,
                sale_of_breeding_lvst TEXT,
                sale_of_mach_and_equip TEXT,
                sale_of_titled_vehicles TEXT,
                sale_of_farm_land TEXT,
                sale_of_farm_buildings TEXT,
                sale_of_other_farm_assets TEXT,
                sale_of_nonfarm_assets TEXT,
                purchase_of_breeding_lvst TEXT,
                purchase_of_mach_and_equip TEXT,
                purchase_of_titled_vehicles TEXT,
                purchase_of_farm_land TEXT,
                purchase_of_farm_buildings TEXT,
                purchase_of_other_farm_assets TEXT,
                purchase_of_nonfarm_assets TEXT,
                cash_from_investing_activities REAL,
                money_borrowed REAL,
                cash_gifts_and_inheritances REAL,
                principal_payments REAL,
                net_nonfarm_income REAL,
                family_living_expense_reported REAL,
                family_living_expense_apparent REAL,
                income_and_soc_sec_tax TEXT,
                dividends_paid TEXT,
                gifts_given TEXT,
                capital_contributions TEXT,
                capital_distributions TEXT,
                cash_from_financing_activities REAL,
                net_change_in_cash_balance REAL,
                ending_cash_balance_calculated REAL,
                ending_cash_balance_reported REAL,
                cash_flow_discrepancy REAL,
                total_capital_sales REAL,
                total_capital_purchases REAL,
                cash_discrepancy_ratio REAL,
                chg_mkt_land_value REAL,
                include_cash_flow_discrepancy TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_prf_lq': '''
            CREATE TABLE fm_prf_lq (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_cap_ad': '''
            CREATE TABLE fm_cap_ad (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_hhold': '''
            CREATE TABLE fm_hhold (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_nf_ie': '''
            CREATE TABLE fm_nf_ie (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_fm_exp': '''
            CREATE TABLE fm_fm_exp (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_fm_inc': '''
            CREATE TABLE fm_fm_inc (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        ''',
        
        'fm_beg_bs_end_bs': '''
            CREATE TABLE fm_beg_bs_end_bs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                fm_genin_guid TEXT,
                hdb_main_data_id TEXT,
                FOREIGN KEY (fm_genin_guid) REFERENCES fm_genin(fm_genin_guid),
                FOREIGN KEY (hdb_main_data_id) REFERENCES hdb_main_data(hdb_main_data_id)
            )
        '''
    }
    
    # Create all tables
    for table_name, schema in schemas.items():
        print(f"Creating table: {table_name}")
        cursor.execute(schema)
    
    print("✅ All tables created successfully!")

def insert_csv_data(cursor, csv_dir):
    """Insert data from CSV files into the database."""
    
    csv_files = {
        'hdb_main_data': 'HdbMainData_sample.csv',
        'fm_genin': 'FM_Genin_sample.csv',
        'fm_guide': 'Fm_Guide_sample.csv',
        'fm_stmts': 'Fm_Stmts_sample.csv'
    }
    
    csv_data_found = False
    
    for table_name, csv_file in csv_files.items():
        csv_path = os.path.join(csv_dir, csv_file)
        if os.path.exists(csv_path):
            try:
                print(f"Inserting data from {csv_file} into {table_name}...")
                df = pd.read_csv(csv_path)
                
                # Handle different CSV structures
                if table_name == 'hdb_main_data':
                    # Skip the first column if it's an index
                    if df.columns[0] == 'Unnamed: 0':
                        df = df.iloc[:, 1:]
                    
                    # Insert data
                    for _, row in df.iterrows():
                        placeholders = ', '.join(['?' for _ in row])
                        columns = ', '.join(row.index)
                        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", tuple(row))
                
                elif table_name in ['fm_genin', 'fm_guide', 'fm_stmts']:
                    # For other tables, insert all columns
                    for _, row in df.iterrows():
                        placeholders = ', '.join(['?' for _ in row])
                        columns = ', '.join(row.index)
                        cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", tuple(row))
                
                print(f"✅ Inserted {len(df)} rows into {table_name}")
                csv_data_found = True
                
            except Exception as e:
                print(f"❌ Error inserting data into {table_name}: {e}")
        else:
            print(f"⚠️  CSV file not found: {csv_file}")
    
    # If no CSV data was found, use sample data instead
    if not csv_data_found:
        print("\n📊 No CSV files found, using sample data instead...")
        insert_sample_data(cursor)

def insert_sample_data(cursor):
    """Insert sample data when CSV files are not available."""
    
    print("Adding sample data to hdb_main_data...")
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
    print("✅ Added 3 farms to hdb_main_data")
    
    print("Adding sample data to fm_genin...")
    cursor.execute("""
        INSERT INTO fm_genin (
            fm_genin_guid, hdb_main_data_id, item_name
        ) VALUES 
        ('guid_001', 'farm_001', 'Johnson Dairy Farm'),
        ('guid_002', 'farm_002', 'Green Valley Corn Farm'),
        ('guid_003', 'farm_003', 'Prairie Wheat Farm')
    """)
    print("✅ Added 3 records to fm_genin")
    
    print("Adding sample data to fm_guide...")
    cursor.execute("""
        INSERT INTO fm_guide (
            item_name, fm_genin_guid, hdb_main_data_id, current_ratio_beg, current_ratio_end,
            working_capital_beg, working_capital_end, net_farm_income_cost, net_farm_income_mkt,
            ebitda_cost, ebitda_mkt, capital_repayment_capacity, capital_repayment_margin,
            term_debt_coverage_ratio_accr, replacement_margin, asset_turnover_rate_cost,
            operating_expense_ratio, interest_expense_ratio, net_farm_income_ratio,
            beg_cost_farm_debt_to_asset_ratio, end_cost_farm_debt_to_asset_ratio,
            beg_mkt_farm_debt_to_asset_ratio, end_mkt_farm_debt_to_asset_ratio
        ) VALUES 
        ('Johnson Dairy Farm', 'guid_001', 'farm_001', 2.1, 2.3, 450000.00, 520000.00, 185000.00, 185000.00,
         225000.00, 225000.00, 'Strong', 0.85, 2.8, 0.12, 0.6, 0.589, 0.089, 0.411, 0.35, 0.32, 0.28, 0.26),
        ('Green Valley Corn Farm', 'guid_002', 'farm_002', 2.8, 3.1, 680000.00, 780000.00, 320000.00, 320000.00,
         380000.00, 380000.00, 'Strong', 0.92, 3.2, 0.15, 0.65, 0.577, 0.077, 0.423, 0.28, 0.25, 0.22, 0.19),
        ('Prairie Wheat Farm', 'guid_003', 'farm_003', 2.4, 2.7, 520000.00, 600000.00, 275000.00, 275000.00,
         325000.00, 325000.00, 'Strong', 0.88, 3.0, 0.13, 0.62, 0.581, 0.081, 0.419, 0.32, 0.29, 0.26, 0.24)
    """)
    print("✅ Added 3 records to fm_guide")
    
    print("Adding sample data to fm_stmts...")
    cursor.execute("""
        INSERT INTO fm_stmts (
            item_name, fm_genin_guid, hdb_main_data_id, beginning_net_worth, net_farm_income, 
            change_in_nonfarm_assets, change_in_nonfarm_accts_payable, other_cash_flows,
            total_change_in_retained_earnings, debts_forgiven, capital_loss_on_repossessions,
            total_change_in_contributed_cap, change_in_mkt_value_of_cap_assets, change_in_deferred_liabilities,
            total_change_in_market_value, total_change_in_net_worth, ending_net_worth_calculated,
            ending_net_worth_reported, equity_discrepancy, beg_cash_balance_farm_and_nonfarm,
            gross_cash_farm_income, total_cash_farm_expense, net_cash_from_hedging, cash_from_operations
        ) VALUES 
        ('Johnson Dairy Farm', 'guid_001', 'farm_001', 1250000.00, 185000.00, 25000.00, -5000.00, 15000.00, 
         'Positive', 0.00, 0.00, 'Stable', 45000.00, -10000.00, 135000.00, 160000.00, 1410000.00, 
         1410000.00, 0.00, 75000.00, 450000.00, 265000.00, 12000.00, 197000.00),
        ('Green Valley Corn Farm', 'guid_002', 'farm_002', 2100000.00, 320000.00, 40000.00, -8000.00, 22000.00, 
         'Positive', 0.00, 0.00, 'Stable', 65000.00, -15000.00, 225000.00, 247000.00, 2347000.00, 
         2347000.00, 0.00, 120000.00, 780000.00, 460000.00, 18000.00, 338000.00),
        ('Prairie Wheat Farm', 'guid_003', 'farm_003', 1800000.00, 275000.00, 35000.00, -6000.00, 18000.00, 
         'Positive', 0.00, 0.00, 'Stable', 55000.00, -12000.00, 195000.00, 218000.00, 2018000.00, 
         2018000.00, 0.00, 95000.00, 620000.00, 345000.00, 15000.00, 292000.00)
    """)
    print("✅ Added 3 records to fm_stmts")
    
    # Add sample data to other tables
    tables_to_populate = [
        ('fm_prf_lq', 'Profitability & Liquidity Analysis'),
        ('fm_cap_ad', 'Capital & Asset Analysis'),
        ('fm_hhold', 'Household Financial Analysis'),
        ('fm_nf_ie', 'Non-Farm Income & Expenses'),
        ('fm_fm_exp', 'Farm Expenses Analysis'),
        ('fm_fm_inc', 'Farm Income Analysis'),
        ('fm_beg_bs_end_bs', 'Balance Sheet Analysis')
    ]
    
    for table_name, description in tables_to_populate:
        print(f"Adding sample data to {table_name}...")
        cursor.execute(f"""
            INSERT INTO {table_name} (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('{description} - Farm 1', 'guid_001', 'farm_001'),
            ('{description} - Farm 2', 'guid_002', 'farm_002'),
            ('{description} - Farm 3', 'guid_003', 'farm_003')
        """)
        print(f"✅ Added 3 records to {table_name}")

def main():
    """Main function to create database and insert data."""
    
    print("🌾 Creating Farm Financial Database")
    print("=" * 50)
    
    # Database file path
    db_path = "finbin_farm_data.db"
    
    # CSV directory path (relative to src directory)
    csv_dir = "../data/samples_v2"
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"🗑️  Removed existing database: {db_path}")
    
    try:
        # Create database connection
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("📊 Creating database schema...")
        create_database_schema(cursor)
        
        print("\n📊 Inserting CSV data...")
        insert_csv_data(cursor, csv_dir)
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        print("\n" + "=" * 50)
        print("🎉 Database created successfully!")
        print(f"📁 Database file: {db_path}")
        print(f"📊 CSV data directory: {csv_dir}")
        
        # Check the created database
        print("\n📊 Checking database contents...")
        check_database_contents(db_path)
        
    except Exception as e:
        print(f"❌ Error creating database: {e}")
        if 'conn' in locals():
            conn.close()

def check_database_contents(db_path):
    """Check the contents of the created database."""
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
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
            print("❌ Database is empty - CSV files may not have been found")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error checking database: {e}")

if __name__ == "__main__":
    main()
