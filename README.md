# FINBIN Farm Data Database

This project creates a SQLite database from FINBIN farm data samples and provides a RAG (Retrieval-Augmented Generation) application for analyzing farm financial data using AI.

## 🚀 Quick Start for First-Time Users

### 1. **Create Virtual Environment:**
```bash
cd /root/projects/ilm_uni
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

### 3. **Create Database and Insert Sample Data:**
```bash
cd src
python3 create_database.py
```

This will:
- Create SQLite database tables with proper schema
- Insert sample data from CSV files in `../data/samples_v2/`
- Create a `finbin_farm_data.db` file

### 4. **Verify Database Creation:**
```bash
python3 check_database.py
```

Expected output:
```
📊 Checking database contents...
==================================================
✅ hdb_main_data: X rows
✅ fm_genin: X rows
✅ fm_guide: X rows
✅ fm_stmts: X rows
...
📈 Total rows across all tables: XX
✅ Database has data!
```

### 5. **View Database Schema (Optional):**
```bash
python3 check_table_schema.py
```

This shows the structure of all tables and their columns.

## 📊 Database Management

### **Create Database from Scratch:**
```bash
cd src
python3 create_database.py
```
- **Use this**: When setting up for the first time
- **What it does**: Creates all tables + inserts CSV data
- **Result**: Fresh database with sample data

### **Add More Sample Data:**
```bash
python3 add_sample_data_minimal.py
```
- **Use this**: To add more test data to existing database
- **What it does**: Inserts additional sample records
- **Result**: More data for testing RAG application

### **Check Database Status:**
```bash
python3 check_database.py          # Quick row count check
python3 check_table_schema.py      # View table structures
```

## 🗄️ Database Schema

The script creates the following tables:

- **hdb_main_data**: Main farm data records (farm IDs, locations, analysts)
- **fm_genin**: Farm general information (farm names, GUIDs)
- **fm_guide**: Financial guide data (ratios, performance metrics)
- **fm_stmts**: Financial statements (income, expenses, cash flow)
- **fm_prf_lq**: Profit and loss data
- **fm_cap_ad**: Capital addition data
- **fm_hhold**: Household data
- **fm_nf_ie**: Non-farm income/expense
- **fm_fm_exp**: Farm expenses
- **fm_fm_inc**: Farm income
- **fm_beg_bs_end_bs**: Beginning and ending balance sheets

## 🔍 Query the Database

### **Using SQLite Command Line:**
```bash
cd src
sqlite3 finbin_farm_data.db
```

Example queries:
```sql
-- View all tables
.tables

-- View table schema
.schema hdb_main_data

-- Query sample data
SELECT * FROM hdb_main_data LIMIT 5;
SELECT * FROM fm_guide LIMIT 5;

-- Count records in each table
SELECT 'hdb_main_data' as table_name, COUNT(*) as count FROM hdb_main_data
UNION ALL
SELECT 'fm_genin', COUNT(*) FROM fm_genin
UNION ALL
SELECT 'fm_guide', COUNT(*) FROM fm_guide;
```

### **Using Python Scripts:**
```bash
# Quick database check
python3 check_database.py

# View detailed schema
python3 check_table_schema.py
```

## 🌟 RAG Application

After setting up the database, you can use the AI-powered RAG application:

### **Quick Test:**
```bash
python3 quick_test.py
```

### **Interactive Demo:**
```bash
python3 demo.py
```

### **Start Web API:**
```bash
python3 farm_rag_api.py
```

For detailed RAG application instructions, see [RAG_README.md](RAG_README.md).

## 📁 File Structure

```
ilm_uni/
├── data/
│   └── samples_v2/              # CSV sample files
├── src/
│   ├── create_database.py        # 🆕 FIRST-TIME SETUP
│   ├── add_sample_data_minimal.py # Add more sample data
│   ├── check_database.py         # Check row counts
│   ├── check_table_schema.py     # View table structures
│   ├── farm_rag_app.py           # Core RAG logic
│   ├── farm_rag_api.py           # FastAPI service
│   ├── web_interface.html        # Web interface
│   ├── quick_test.py             # Quick test
│   ├── test_rag_app.py           # Full test suite
│   ├── demo.py                   # Interactive demo
│   └── finbin_farm_data.db       # SQLite database
├── FINBIN Data Dictionary Farm.xlsx  # Data dictionary
├── requirements.txt               # Python dependencies
├── README.md                     # This file
└── RAG_README.md                 # RAG application guide
```

## 🔧 Troubleshooting

### **Common Issues:**

1. **"Database file not found"**
   - Run `python3 create_database.py` first
   - Check you're in the `src/` directory

2. **"No module named 'pandas'"**
   - Activate virtual environment: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`

3. **"CSV files not found"**
   - Ensure CSV files exist in `../data/samples_v2/`
   - Check file names match: `HdbMainData_sample.csv`, `FM_Genin_sample.csv`, etc.

4. **"Permission denied"**
   - Check file permissions: `chmod +x *.py`
   - Ensure write access to `src/` directory

### **Verification Steps:**

1. **Check CSV files exist:**
   ```bash
   ls -la ../data/samples_v2/
   ```

2. **Verify database creation:**
   ```bash
   python3 check_database.py
   ```

3. **Check table schemas:**
   ```bash
   python3 check_table_schema.py
   ```

## 📚 Next Steps

After successfully creating the database:

1. **Test the RAG application**: `python3 quick_test.py`
2. **Run interactive demo**: `python3 demo.py`
3. **Start web interface**: `python3 farm_rag_api.py`
4. **Read RAG guide**: [RAG_README.md](RAG_README.md)

## 📖 Data Sources

- **Excel Dictionary**: Contains table definitions and field descriptions
- **CSV Samples**: Sample data files for each table type
- **Database**: SQLite database with relational structure and foreign keys

## 📝 Notes

- The script automatically handles column name cleaning (spaces to underscores, special characters)
- Foreign key relationships are maintained between tables
- Data types are inferred from the sample data
- The database is created in the `src/` directory
- Sample data includes 3 test farms with realistic financial metrics