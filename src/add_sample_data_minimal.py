#!/usr/bin/env python3
"""
Minimal Script to add basic sample data to the database tables.
Only inserts into tables with simple schemas to avoid column count issues.
"""

import sqlite3
import os

def clean_existing_data():
    """Clean all existing data from the database tables."""
    
    db_path = "finbin_farm_data.db"
    
    if not os.path.exists(db_path):
        print(f"❌ Database file not found: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("🧹 Cleaning existing data from database...")
        print("=" * 50)
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            if table_name == 'sqlite_sequence':  # Skip system table
                continue
            try:
                cursor.execute(f"DELETE FROM {table_name}")
                print(f"🧹 Cleaned {table_name}")
            except Exception as e:
                print(f"❌ Error cleaning {table_name}: {e}")
        
        # Reset auto-increment sequences
        cursor.execute("DELETE FROM sqlite_sequence")
        
        # Commit changes
        conn.commit()
        conn.close()
        
        print("✅ Database cleaned successfully!")
        
    except Exception as e:
        print(f"❌ Error cleaning database: {e}")
        if 'conn' in locals():
            conn.close()

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
             'Prairie Wheat Farm', 'Fargo, ND', 'N'),
            ('farm_004', 'file_004', 'tenant_004', 'org_004', 
             'branch_004', 'IA', 'banker_004', 'Sarah Wilson', 'Analyst D', 
             'farm_004', 'finbin_004', '2021', 'dataset_004', 'source_004', 
             '2023-04-15', 'analysis_004', '2021', 'IA', 'Polk', 
             'Iowa Soybean Farm', 'Des Moines, IA', 'N'),
            ('farm_005', 'file_005', 'tenant_005', 'org_005', 
             'branch_005', 'IL', 'banker_005', 'Mike Brown', 'Analyst E', 
             'farm_005', 'finbin_005', '2021', 'dataset_005', 'source_005', 
             '2023-05-20', 'analysis_005', '2021', 'IL', 'McLean', 
             'Central Illinois Grain Farm', 'Bloomington, IL', 'N'),
            ('farm_006', 'file_006', 'tenant_006', 'org_006', 
             'branch_006', 'KS', 'banker_006', 'Lisa Davis', 'Analyst F', 
             'farm_006', 'finbin_006', '2021', 'dataset_006', 'source_006', 
             '2023-06-10', 'analysis_006', '2021', 'KS', 'Sedgwick', 
             'Kansas Cattle Ranch', 'Wichita, KS', 'N'),
            ('farm_007', 'file_007', 'tenant_007', 'org_007', 
             'branch_007', 'NE', 'banker_007', 'Tom Miller', 'Analyst G', 
             'farm_007', 'finbin_007', '2021', 'dataset_007', 'source_007', 
             '2023-07-15', 'analysis_007', '2021', 'NE', 'Lancaster', 
             'Nebraska Hog Farm', 'Lincoln, NE', 'N'),
            ('farm_008', 'file_008', 'tenant_008', 'org_008', 
             'branch_008', 'SD', 'banker_008', 'Amy Johnson', 'Analyst H', 
             'farm_008', 'finbin_008', '2021', 'dataset_008', 'source_008', 
             '2023-08-20', 'analysis_008', '2021', 'SD', 'Minnehaha', 
             'South Dakota Sheep Farm', 'Sioux Falls, SD', 'N'),
            ('farm_009', 'file_009', 'tenant_009', 'org_009', 
             'branch_009', 'MO', 'banker_009', 'David Lee', 'Analyst I', 
             'farm_009', 'finbin_009', '2021', 'dataset_009', 'source_009', 
             '2023-09-25', 'analysis_009', '2021', 'MO', 'Boone', 
             'Missouri Poultry Farm', 'Columbia, MO', 'N'),
            ('farm_010', 'file_010', 'tenant_010', 'org_010', 
             'branch_010', 'OH', 'banker_010', 'Karen White', 'Analyst J', 
             'farm_010', 'finbin_010', '2021', 'dataset_010', 'source_010', 
             '2023-10-30', 'analysis_010', '2021', 'OH', 'Franklin', 
             'Ohio Vegetable Farm', 'Columbus, OH', 'N')
        """)
        print("✅ Added 10 farms to hdb_main_data")
        
        # Add sample data to fm_genin (3 columns - confirmed working)
        print("Adding data to fm_genin...")
        cursor.execute("""
            INSERT INTO fm_genin (
                fm_genin_guid, hdb_main_data_id, item_name
            ) VALUES 
            ('guid_001', 'farm_001', 'Johnson Dairy Farm'),
            ('guid_002', 'farm_002', 'Green Valley Corn Farm'),
            ('guid_003', 'farm_003', 'Prairie Wheat Farm'),
            ('guid_004', 'farm_004', 'Iowa Soybean Farm'),
            ('guid_005', 'farm_005', 'Central Illinois Grain Farm'),
            ('guid_006', 'farm_006', 'Kansas Cattle Ranch'),
            ('guid_007', 'farm_007', 'Nebraska Hog Farm'),
            ('guid_008', 'farm_008', 'South Dakota Sheep Farm'),
            ('guid_009', 'farm_009', 'Missouri Poultry Farm'),
            ('guid_010', 'farm_010', 'Ohio Vegetable Farm')
        """)
        print("✅ Added 10 records to fm_genin")
        
        # Add sample data to fm_guide with key performance metrics (simplified approach)
        print("Adding data to fm_guide...")
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
             325000.00, 325000.00, 'Strong', 0.88, 3.0, 0.13, 0.62, 0.581, 0.081, 0.419, 0.32, 0.29, 0.26, 0.24),
            ('Iowa Soybean Farm', 'guid_004', 'farm_004', 2.2, 2.5, 480000.00, 550000.00, 240000.00, 240000.00,
             290000.00, 290000.00, 'Strong', 0.86, 2.9, 0.11, 0.59, 0.586, 0.086, 0.414, 0.35, 0.32, 0.30, 0.28),
            ('Central Illinois Grain Farm', 'guid_005', 'farm_005', 2.6, 2.9, 620000.00, 710000.00, 290000.00, 290000.00,
             350000.00, 350000.00, 'Strong', 0.90, 3.1, 0.14, 0.63, 0.583, 0.083, 0.417, 0.30, 0.27, 0.25, 0.23),
            ('Kansas Cattle Ranch', 'guid_006', 'farm_006', 1.9, 2.1, 380000.00, 430000.00, 195000.00, 195000.00,
             245000.00, 245000.00, 'Moderate', 0.78, 2.6, 0.09, 0.54, 0.593, 0.093, 0.407, 0.40, 0.37, 0.35, 0.33),
            ('Nebraska Hog Farm', 'guid_007', 'farm_007', 1.7, 1.9, 320000.00, 360000.00, 165000.00, 165000.00,
             215000.00, 215000.00, 'Moderate', 0.75, 2.4, 0.08, 0.52, 0.595, 0.095, 0.405, 0.42, 0.39, 0.37, 0.35),
            ('South Dakota Sheep Farm', 'guid_008', 'farm_008', 1.5, 1.7, 250000.00, 280000.00, 125000.00, 125000.00,
             175000.00, 175000.00, 'Weak', 0.68, 2.1, 0.06, 0.47, 0.602, 0.102, 0.398, 0.48, 0.45, 0.43, 0.41),
            ('Missouri Poultry Farm', 'guid_009', 'farm_009', 1.8, 2.0, 290000.00, 330000.00, 145000.00, 145000.00,
             195000.00, 195000.00, 'Moderate', 0.72, 2.3, 0.07, 0.49, 0.600, 0.100, 0.400, 0.45, 0.42, 0.40, 0.38),
            ('Ohio Vegetable Farm', 'guid_010', 'farm_010', 2.0, 2.3, 350000.00, 400000.00, 175000.00, 175000.00,
             225000.00, 225000.00, 'Moderate', 0.80, 2.7, 0.10, 0.51, 0.598, 0.098, 0.402, 0.38, 0.35, 0.33, 0.31)
        """)
        print("✅ Added 10 records to fm_guide with key performance metrics")
        
        # Add sample data to fm_stmts with financial data
        print("Adding data to fm_stmts...")
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
             2018000.00, 0.00, 95000.00, 620000.00, 345000.00, 15000.00, 292000.00),
            ('Iowa Soybean Farm', 'guid_004', 'farm_004', 1650000.00, 240000.00, 30000.00, -7000.00, 16000.00, 
             'Positive', 0.00, 0.00, 'Stable', 50000.00, -11000.00, 175000.00, 199000.00, 1849000.00, 
             1849000.00, 0.00, 85000.00, 580000.00, 340000.00, 14000.00, 256000.00),
            ('Central Illinois Grain Farm', 'guid_005', 'farm_005', 1950000.00, 290000.00, 38000.00, -9000.00, 20000.00, 
             'Positive', 0.00, 0.00, 'Stable', 60000.00, -13000.00, 210000.00, 235000.00, 2185000.00, 
             2185000.00, 0.00, 110000.00, 720000.00, 430000.00, 17000.00, 307000.00),
            ('Kansas Cattle Ranch', 'guid_006', 'farm_006', 1400000.00, 195000.00, 25000.00, -4000.00, 12000.00, 
             'Positive', 0.00, 0.00, 'Stable', 40000.00, -8000.00, 150000.00, 167000.00, 1567000.00, 
             1567000.00, 0.00, 70000.00, 420000.00, 225000.00, 10000.00, 207000.00),
            ('Nebraska Hog Farm', 'guid_007', 'farm_007', 1200000.00, 165000.00, 20000.00, -3000.00, 10000.00, 
             'Positive', 0.00, 0.00, 'Stable', 35000.00, -6000.00, 125000.00, 139000.00, 1339000.00, 
             1339000.00, 0.00, 60000.00, 380000.00, 215000.00, 8000.00, 173000.00),
            ('South Dakota Sheep Farm', 'guid_008', 'farm_008', 950000.00, 125000.00, 15000.00, -2000.00, 8000.00, 
             'Positive', 0.00, 0.00, 'Stable', 25000.00, -4000.00, 95000.00, 103000.00, 1053000.00, 
             1053000.00, 0.00, 45000.00, 280000.00, 155000.00, 6000.00, 131000.00),
            ('Missouri Poultry Farm', 'guid_009', 'farm_009', 1100000.00, 145000.00, 18000.00, -2500.00, 9000.00, 
             'Positive', 0.00, 0.00, 'Stable', 30000.00, -5000.00, 110000.00, 118000.00, 1218000.00, 
             1218000.00, 0.00, 55000.00, 320000.00, 175000.00, 7000.00, 152000.00),
            ('Ohio Vegetable Farm', 'guid_010', 'farm_010', 1350000.00, 175000.00, 22000.00, -3500.00, 11000.00, 
             'Positive', 0.00, 0.00, 'Stable', 38000.00, -7000.00, 130000.00, 143000.00, 1493000.00, 
             1493000.00, 0.00, 65000.00, 380000.00, 205000.00, 9000.00, 186000.00)
        """)
        print("✅ Added 10 records to fm_stmts with financial data")
        
        # Add sample data to other tables with financial metrics
        print("Adding data to fm_prf_lq (Profitability & Liquidity)...")
        cursor.execute("""
            INSERT INTO fm_prf_lq (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Current Ratio Analysis', 'guid_001', 'farm_001'),
            ('Working Capital Analysis', 'guid_002', 'farm_002'),
            ('Debt-to-Asset Analysis', 'guid_003', 'farm_003'),
            ('Return on Assets Analysis', 'guid_004', 'farm_004'),
            ('Profit Margin Analysis', 'guid_005', 'farm_005'),
            ('Liquidity Analysis', 'guid_006', 'farm_006'),
            ('Solvency Analysis', 'guid_007', 'farm_007'),
            ('Efficiency Analysis', 'guid_008', 'farm_008'),
            ('Risk Assessment', 'guid_009', 'farm_009'),
            ('Performance Benchmarking', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_prf_lq")
        
        print("Adding data to fm_cap_ad (Capital & Assets)...")
        cursor.execute("""
            INSERT INTO fm_cap_ad (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Asset Valuation', 'guid_001', 'farm_001'),
            ('Capital Structure', 'guid_002', 'farm_002'),
            ('Investment Analysis', 'guid_003', 'farm_003'),
            ('Depreciation Schedule', 'guid_004', 'farm_004'),
            ('Asset Turnover', 'guid_005', 'farm_005'),
            ('Capital Efficiency', 'guid_006', 'farm_006'),
            ('Asset Management', 'guid_007', 'farm_007'),
            ('Investment Returns', 'guid_008', 'farm_008'),
            ('Capital Allocation', 'guid_009', 'farm_009'),
            ('Asset Performance', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_cap_ad")
        
        print("Adding data to fm_hhold (Household)...")
        cursor.execute("""
            INSERT INTO fm_hhold (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Family Living Expenses', 'guid_001', 'farm_001'),
            ('Household Income', 'guid_002', 'farm_002'),
            ('Personal Financial Planning', 'guid_003', 'farm_003'),
            ('Tax Planning', 'guid_004', 'farm_004'),
            ('Retirement Planning', 'guid_005', 'farm_005'),
            ('Insurance Coverage', 'guid_006', 'farm_006'),
            ('Estate Planning', 'guid_007', 'farm_007'),
            ('Succession Planning', 'guid_008', 'farm_008'),
            ('Risk Management', 'guid_009', 'farm_009'),
            ('Financial Education', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_hhold")
        
        print("Adding data to fm_nf_ie (Non-Farm Income & Expenses)...")
        cursor.execute("""
            INSERT INTO fm_nf_ie (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Off-Farm Employment', 'guid_001', 'farm_001'),
            ('Investment Income', 'guid_002', 'farm_002'),
            ('Rental Income', 'guid_003', 'farm_003'),
            ('Business Income', 'guid_004', 'farm_004'),
            ('Interest Income', 'guid_005', 'farm_005'),
            ('Dividend Income', 'guid_006', 'farm_006'),
            ('Capital Gains', 'guid_007', 'farm_007'),
            ('Other Income', 'guid_008', 'farm_008'),
            ('Non-Farm Expenses', 'guid_009', 'farm_009'),
            ('Tax Deductions', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_nf_ie")
        
        print("Adding data to fm_fm_exp (Farm Expenses)...")
        cursor.execute("""
            INSERT INTO fm_fm_exp (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Feed Costs', 'guid_001', 'farm_001'),
            ('Seed Costs', 'guid_002', 'farm_002'),
            ('Fertilizer Costs', 'guid_003', 'farm_003'),
            ('Chemical Costs', 'guid_004', 'farm_004'),
            ('Fuel Costs', 'guid_005', 'farm_005'),
            ('Repair Costs', 'guid_006', 'farm_006'),
            ('Labor Costs', 'guid_007', 'farm_007'),
            ('Insurance Costs', 'guid_008', 'farm_008'),
            ('Interest Expenses', 'guid_009', 'farm_009'),
            ('Depreciation', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_fm_exp")
        
        print("Adding data to fm_fm_inc (Farm Income)...")
        cursor.execute("""
            INSERT INTO fm_fm_inc (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Crop Sales', 'guid_001', 'farm_001'),
            ('Livestock Sales', 'guid_002', 'farm_002'),
            ('Dairy Sales', 'guid_003', 'farm_003'),
            ('Government Payments', 'guid_004', 'farm_004'),
            ('Insurance Proceeds', 'guid_005', 'farm_005'),
            ('Custom Work', 'guid_006', 'farm_006'),
            ('Rental Income', 'guid_007', 'farm_007'),
            ('Other Farm Income', 'guid_008', 'farm_008'),
            ('Grain Sales', 'guid_009', 'farm_009'),
            ('Produce Sales', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_fm_inc")
        
        print("Adding data to fm_beg_bs_end_bs (Balance Sheet)...")
        cursor.execute("""
            INSERT INTO fm_beg_bs_end_bs (
                item_name, fm_genin_guid, hdb_main_data_id
            ) VALUES 
            ('Beginning Assets', 'guid_001', 'farm_001'),
            ('Ending Assets', 'guid_002', 'farm_002'),
            ('Beginning Liabilities', 'guid_003', 'farm_003'),
            ('Ending Liabilities', 'guid_004', 'farm_004'),
            ('Beginning Equity', 'guid_005', 'farm_005'),
            ('Ending Equity', 'guid_006', 'farm_006'),
            ('Asset Changes', 'guid_007', 'farm_007'),
            ('Liability Changes', 'guid_008', 'farm_008'),
            ('Equity Changes', 'guid_009', 'farm_009'),
            ('Net Worth Analysis', 'guid_010', 'farm_010')
        """)
        print("✅ Added 10 records to fm_beg_bs_end_bs")
        
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
            print(f"📊 Expected: 100 rows (10 farms × 10 tables)")
            print(f"📊 Actual: {total_rows} rows")
        else:
            print("❌ Database is still empty")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error checking data: {e}")

def main():
    """Main function."""
    print("🌾 Adding Sample Data to Farm Financial Database (Enhanced Version)")
    print("=" * 70)
    
    # Clean existing data first
    clean_existing_data()
    
    print("\n" + "=" * 70)
    
    # Add sample data
    add_sample_data()
    
    print("\n" + "=" * 70)
    
    # Check the data
    check_data()

if __name__ == "__main__":
    main()
