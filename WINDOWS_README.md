# 🌾 Farm Financial Data RAG Application - Windows Setup

AI-powered farm financial data analysis. Ask questions in plain English and get intelligent insights about farm performance.

## 🎯 What This Application Does

- **Ask Questions**: "Which farms had the highest net farm income?" or "Show me farms with the best debt ratios"
- **AI Analysis**: Automatically generates SQL queries and provides financial insights
- **Web Interface**: User-friendly browser interface at http://localhost:8000/web_interface.html

## 📋 Prerequisites

- ✅ **Windows 10/11** (64-bit)
- ✅ **Python 3.11+** ([Download](https://www.python.org/downloads/)) - **Check "Add Python to PATH"**
- ✅ **Git** ([Download](https://git-scm.com/download/win))
- ✅ **OpenAI API key** ([Get one here](https://platform.openai.com/api-keys))

## 🚀 Quick Start

### **One-Click Setup (Recommended)**

1. **Install Python & Git** (see Prerequisites above)
2. **Clone the repository**:
   ```cmd
   git clone https://github.com/yourusername/ilm_uni.git
   cd ilm_uni
   ```
3. **Double-click `user_setup.bat`**
4. **Follow the prompts** - everything else is automated!

**What happens automatically:**
- ✅ Creates Python virtual environment
- ✅ Installs dependencies
- ✅ Creates database with sample data
- ✅ Launches web interface in browser

## 🎮 Running the Application

### **After Setup (Daily Usage)**

**To start the application:**
1. **Navigate to project folder**: `cd ilm_uni`
2. **Double-click `user_setup.bat`** (or run manually below)

**Manual start:**
```cmd
cd ilm_uni
venv\Scripts\activate
cd src
python farm_rag_api.py
```
Then open: http://localhost:8000/web_interface.html

**To stop:** Press `Ctrl + C` in the command prompt

## 💡 Example Questions to Try

### **Start Simple:**
- "How many farms are in the database?"
- "What are the names of all farms?"
- "Which states have farms?"

### **Financial Analysis:**
- "Which farms have the highest current ratio?"
- "What is the average working capital?"
- "Show me farms with the best debt-to-equity ratios"
- "Which farms had the highest net farm income?"

### **Geographic Queries:**
- "How many farms are in each state?"
- "Compare farm performance between different counties"
- "What's the average financial performance by region?"

## 🔧 Troubleshooting

### **Common Issues:**

**"python is not recognized"**
- Reinstall Python and check "Add Python to PATH"
- Restart Command Prompt

**"No module named 'openai'"**
- Activate virtual environment: `venv\Scripts\activate`
- Install dependencies: `pip install -r requirements.txt`

**"Database file not found"**
- Run: `cd src && python create_database.py`

**"OpenAI API key not configured"**
- Check `.env` file exists with valid API key starting with `sk-`

**"Port 8000 already in use"**
- Close other applications using port 8000

## 📁 Project Structure

```
ilm_uni/
├── user_setup.bat              # 🚀 Main setup file
├── requirements.txt            # Python dependencies
├── src/
│   ├── farm_rag_api.py        # Web server
│   ├── farm_rag_app.py        # Core RAG logic
│   ├── create_database.py     # Database setup
│   ├── web_interface.html     # Web UI
│   └── finbin_farm_data.db    # SQLite database
├── venv/                      # Python virtual environment
└── .env                       # API configuration
```

## 🎯 Tips for Best Results

- **Be Specific**: "Which farms in Minnesota have current ratios above 2.0?"
- **Use Financial Terms**: "debt-to-equity ratio", "working capital", "net farm income"
- **Ask for Comparisons**: "Compare dairy vs grain farm performance"

---

**🎉 Ready to analyze farm financial data with AI!**

Start by double-clicking `user_setup.bat` and asking questions like:
- "Which farms had the highest net farm income?"
- "Show me farms with the best debt ratios"
- "What's the average working capital by state?"
