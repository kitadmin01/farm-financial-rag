# 🌾 FINBIN Farm Financial Data RAG Application

An AI-powered RAG (Retrieval-Augmented Generation) application that uses OpenAI's LLM to analyze farm financial data. Users can ask natural language questions about farm performance, and the system will generate SQL queries, execute them against the SQLite database, and provide intelligent insights.

## 🚀 Quick Start for First-Time Users

### **Prerequisites Check:**
Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ OpenAI API key (get from [OpenAI Platform](https://platform.openai.com/))
- ✅ CSV sample files in `data/samples_v2/`

### **Step 1: Create Virtual Environment**
```bash
cd /root/projects/ilm_uni
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Create Database and Insert Sample Data**
```bash
cd src
python3 create_database.py
```

This will:
- Create SQLite database tables with proper schema
- Insert sample data from CSV files in `../data/samples_v2/`
- Create a `finbin_farm_data.db` file

### **Step 4: Verify Database Creation**
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

### **Step 5: Configure OpenAI API**
```bash
cd ..
# Create .env file
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
echo "DATABASE_PATH=finbin_farm_data.db" >> .env
```

### **Step 6: Test the RAG Application**
```bash
cd src
python3 quick_test.py
```

Expected output:
```
🌾 Testing Farm Financial RAG Application
==========================================
✅ Database connection successful
✅ Database has data (XX rows)
✅ OpenAI API key configured
✅ RAG application ready!
```

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

## 🌟 RAG Application Features

- **Natural Language Processing**: Ask questions in plain English about farm financial data
- **AI-Generated SQL**: OpenAI LLM automatically generates appropriate SQL queries
- **Intelligent Responses**: Get contextual, financial analysis with insights and recommendations
- **Multiple Interfaces**: Command-line, REST API, and web interface options
- **Real-time Analysis**: Execute queries and get instant results
- **Data Visualization**: View query results in formatted tables

## 🏗️ RAG Architecture

```
User Question → OpenAI LLM → SQL Generation → SQLite Execution → Data Analysis → AI Response
```

1. **Question Understanding**: OpenAI analyzes the user's natural language question
2. **SQL Generation**: LLM generates appropriate SQL based on database schema
3. **Query Execution**: SQL is executed against the SQLite database
4. **Data Analysis**: Results are processed and formatted
5. **Intelligent Response**: OpenAI generates insights and explanations

## 🚀 Running the RAG Application

### **Option 1: Quick Test (Recommended for First Time)**
```bash
cd src
python3 quick_test.py
```
- **Best for**: First-time users to verify everything works
- **What it does**: Tests database, OpenAI API, and basic RAG functionality
- **Time**: ~30 seconds

### **Option 2: Interactive Demo**
```bash
cd src
python3 demo.py
```
- **Best for**: Exploring the application interactively
- **What it does**: Guided tour with example questions
- **Time**: 5-10 minutes

### **Option 3: Web Interface**
```bash
cd src
python3 farm_rag_api.py
```
- **Best for**: Web-based interaction
- **What it does**: Starts FastAPI server with web interface
- **Access**: http://localhost:8000/web_interface.html

### **Option 4: Command Line Interface**
```bash
cd src
python3 farm_rag_app.py
```
- **Best for**: Direct command-line interaction
- **What it does**: Interactive CLI for asking questions
- **Time**: Continuous session

### **Option 5: Automated Startup Script**
```bash
./start_rag_app.sh
```
- **Best for**: Production-like startup
- **What it does**: Activates venv, installs deps, starts API server
- **Result**: Full RAG application running

## 🌐 Web Interface & API

Once the API server is running, access:

- **Web Interface**: http://localhost:8000/web_interface.html
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### **API Endpoints**

#### POST /ask
Ask a question about farm financial data.

**Request:**
```json
{
  "question": "Which farms have the highest current ratio?",
  "include_data_preview": true,
  "max_preview_rows": 10
}
```

**Response:**
```json
{
  "success": true,
  "question": "Which farms have the highest current ratio?",
  "sql_query": "SELECT ...",
  "response": "Based on the analysis...",
  "query_result": {
    "success": true,
    "row_count": 10,
    "execution_time": 0.123
  },
  "data_preview": [...]
}
```

#### GET /schema
Get database schema information.

#### GET /examples
Get example questions users can ask.

#### GET /health
Health check endpoint.

## 💡 Example Questions

### **Start with Simple Questions:**
- "How many farms are in the database?"
- "What are the names of all farms?"
- "Which states have farms?"

### **Financial Performance:**
- "Which farms have the highest current ratio?"
- "What is the average working capital by state?"
- "Show me farms with the best debt-to-equity ratios"
- "Which farms had the highest net farm income?"

### **Geographic Analysis:**
- "How many farms are in each state?"
- "What's the average financial performance by county?"
- "Compare farm performance between Minnesota and Wisconsin"

### **Trends and Changes:**
- "How did net worth change from beginning to end of year?"
- "Which farms had the biggest increase in working capital?"
- "Show me farms with significant changes in debt levels"

### **Benchmarking:**
- "What's the 75th percentile for current ratio?"
- "How do farms rank by return on assets?"
- "Which farms are in the top 10% for profitability?"

## 🧪 Testing Your Setup

### **Quick Verification:**
```bash
cd src
python3 quick_test.py
```

### **Comprehensive Testing:**
```bash
python3 test_rag_app.py
```
This runs all 10 comprehensive tests including performance testing.

### **Interactive Demo:**
```bash
python3 demo.py
```
Choose between automated demo or interactive question-asking mode.

### **Expected Results:**
- ✅ Database connection successful
- ✅ Database has data
- ✅ OpenAI API key configured
- ✅ RAG application ready

## 🔧 Configuration

### **Environment Variables**

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `DATABASE_PATH` | Path to SQLite database | `finbin_farm_data.db` |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-3.5-turbo` |
| `MAX_TOKENS` | Maximum tokens for responses | `1000` |
| `TEMPERATURE` | Response creativity (0-1) | `0.7` |

### **Database Schema**

The application automatically detects and uses the database schema from your SQLite database. Tables include:

- `hdb_main_data`: Main farm data records
- `fm_genin`: Farm general information
- `fm_guide`: Financial guide data
- `fm_stmts`: Financial statements
- `fm_prf_lq`: Profit and loss data
- And more...

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
├── start_rag_app.sh              # Startup script
├── .env                          # Environment variables
└── README.md                     # This file
```

## 🐛 Troubleshooting

### **Common Issues**

1. **OpenAI API Key Error**
   ```bash
   # Check .env file
   cat .env
   
   # Ensure API key is correct
   echo "OPENAI_API_KEY=your_actual_key" > .env
   ```

2. **Database Not Found**
   ```bash
   cd src
   python3 create_database.py
   python3 check_database.py
   ```

3. **Import Errors**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Port Already in Use**
   ```bash
   # Kill existing process
   pkill -f farm_rag_api
   
   # Or change port in farm_rag_api.py
   ```

5. **"Database file not found"**
   - Run `python3 create_database.py` first
   - Check you're in the `src/` directory

6. **"No module named 'pandas'"**
   - Activate virtual environment: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`

7. **"CSV files not found"**
   - Ensure CSV files exist in `../data/samples_v2/`
   - Check file names match: `HdbMainData_sample.csv`, `FM_Genin_sample.csv`, etc.

8. **"Permission denied"**
   - Check file permissions: `chmod +x *.py`
   - Ensure write access to `src/` directory

### **Debug Mode**

Enable detailed logging by modifying the logging level in the Python files:

```python
logging.basicConfig(level=logging.DEBUG)
```

### **Verification Checklist:**

- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Database created (`python3 create_database.py`)
- [ ] Database has data (`python3 check_database.py`)
- [ ] `.env` file with OpenAI API key
- [ ] Quick test passes (`python3 quick_test.py`)

## 📊 Performance

- **SQL Generation**: ~2-5 seconds (depends on OpenAI API response time)
- **Query Execution**: <1 second for typical queries
- **Response Generation**: ~3-8 seconds (depends on data size and OpenAI API)
- **Total Response Time**: Typically 5-15 seconds

### **Expected Performance**
- **Simple Queries**: 3-8 seconds
- **Complex Queries**: 8-15 seconds
- **Database Queries**: <1 second
- **OpenAI API Calls**: 2-8 seconds

### **Performance Optimization**
- Use appropriate model (gpt-3.5-turbo for testing, gpt-4 for production)
- Optimize database queries
- Implement caching for repeated questions
- Monitor API usage and costs

## 🔒 Security Considerations

- Keep your OpenAI API key secure
- The database contains sample data only
- API endpoints are not authenticated (for development use)
- Consider adding authentication for production use

## 🚀 Future Enhancements

- [ ] User authentication and session management
- [ ] Query caching for improved performance
- [ ] Advanced data visualization (charts, graphs)
- [ ] Export functionality (PDF reports, Excel)
- [ ] Batch question processing
- [ ] Integration with additional data sources

## 📞 Support

For issues or questions:

1. **Check the troubleshooting section above**
2. **Verify your setup step by step**
3. **Review the API documentation at `/docs`**
4. **Check the application logs**
5. **Verify your OpenAI API key and credits**

## 📄 License

This project is for educational and development purposes. Ensure compliance with OpenAI's terms of service and data usage policies.

## 🔄 Next Steps After Setup

1. **Test basic functionality**: `python3 quick_test.py`
2. **Explore interactively**: `python3 demo.py`
3. **Use web interface**: `python3 farm_rag_api.py`
4. **Ask your own questions** about farm financial data
5. **Customize the application** for your specific needs

## 📖 Data Sources

- **Excel Dictionary**: Contains table definitions and field descriptions
- **CSV Samples**: Sample data files for each table type
- **Database**: SQLite database with relational structure and foreign keys

## 📝 Notes

- The script automatically handles column name cleaning (spaces to underscores, special characters)
- Foreign key relationships are maintained between tables
- Data types are inferred from the sample data
- The database is created in the `src/` directory
- Sample data includes 10 diverse farms with realistic financial metrics
- The RAG application provides intelligent financial analysis and insights

---

**Happy Farming! 🌾✨**

Your RAG application should provide intelligent farm financial analysis once all tests pass.