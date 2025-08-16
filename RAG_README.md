# 🌾 Farm Financial Data RAG Application

An AI-powered RAG (Retrieval-Augmented Generation) application that uses OpenAI's LLM to analyze farm financial data. Users can ask natural language questions about farm performance, and the system will generate SQL queries, execute them against the SQLite database, and provide intelligent insights.

## 🚀 Quick Start for First-Time Users

### **Prerequisites Check:**
Before starting, ensure you have:
- ✅ Python 3.8+ installed
- ✅ OpenAI API key (get from [OpenAI Platform](https://platform.openai.com/))
- ✅ Database created with sample data

### **Step 1: Database Setup (If Not Done)**
```bash
cd /root/projects/ilm_uni/src
python3 create_database.py
python3 check_database.py  # Verify data exists
```

### **Step 2: Environment Setup**
```bash
cd /root/projects/ilm_uni
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **Step 3: Configure OpenAI API**
```bash
# Create .env file
echo "OPENAI_API_KEY=your_actual_api_key_here" > .env
echo "DATABASE_PATH=finbin_farm_data.db" >> .env
```

### **Step 4: Test the RAG Application**
```bash
cd src
python3 quick_test.py
```

Expected output:
```
🌾 Testing Farm Financial RAG Application
==========================================
✅ Database connection successful
✅ Database has data (33 rows)
✅ OpenAI API key configured
✅ RAG application ready!
```

## 🚀 Running the Application

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

## 🌟 Features

- **Natural Language Processing**: Ask questions in plain English about farm financial data
- **AI-Generated SQL**: OpenAI LLM automatically generates appropriate SQL queries
- **Intelligent Responses**: Get contextual, financial analysis with insights and recommendations
- **Multiple Interfaces**: Command-line, REST API, and web interface options
- **Real-time Analysis**: Execute queries and get instant results
- **Data Visualization**: View query results in formatted tables

## 🏗️ Architecture

```
User Question → OpenAI LLM → SQL Generation → SQLite Execution → Data Analysis → AI Response
```

1. **Question Understanding**: OpenAI analyzes the user's natural language question
2. **SQL Generation**: LLM generates appropriate SQL based on database schema
3. **Query Execution**: SQL is executed against the SQLite database
4. **Data Analysis**: Results are processed and formatted
5. **Intelligent Response**: OpenAI generates insights and explanations

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- SQLite database with sample data (created via `create_database.py`)

## 🛠️ Installation & Setup

### 1. **Clone and Setup Environment**

```bash
# Navigate to project directory
cd /root/projects/ilm_uni

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. **Configure Environment**

```bash
# Create .env file
nano .env
```

Add your OpenAI API key:
```env
OPENAI_API_KEY=your_actual_api_key_here
DATABASE_PATH=finbin_farm_data.db
```

### 3. **Verify Database Setup**

```bash
cd src
python3 check_database.py
```

Ensure you see:
```
✅ Database has data!
📈 Total rows across all tables: 33
```

## 🔍 Testing Your Setup

### **Quick Verification:**
```bash
cd src
python3 quick_test.py
```

### **Expected Results:**
- ✅ Database connection successful
- ✅ Database has data
- ✅ OpenAI API key configured
- ✅ RAG application ready

### **If You See Errors:**

1. **"Database file not found"**
   ```bash
   python3 create_database.py
   ```

2. **"OpenAI API key not found"**
   ```bash
   # Check .env file exists and has correct API key
   cat .env
   ```

3. **"No module named 'openai'"**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 🌐 Web Interface

Once the API server is running, access the web interface:

- **Web Interface**: http://localhost:8000/web_interface.html
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📱 API Endpoints

### POST /ask
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

### GET /schema
Get database schema information.

### GET /examples
Get example questions users can ask.

### GET /health
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

## 🔧 Configuration

### **Environment Variables**

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `DATABASE_PATH` | Path to SQLite database | `finbin_farm_data.db` |

### **Database Schema**

The application automatically detects and uses the database schema from your SQLite database. Tables include:

- `hdb_main_data`: Main farm data records
- `fm_genin`: Farm general information
- `fm_guide`: Financial guide data
- `fm_stmts`: Financial statements
- `fm_prf_lq`: Profit and loss data
- And more...

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
