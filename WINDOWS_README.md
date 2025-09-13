# 🌾 Windows Installation Guide - Farm Financial Data RAG Application

This guide will walk you through installing and running the Farm Financial Data RAG Application on Windows. This application uses AI to analyze farm financial data - you can ask questions in plain English and get intelligent insights about farm performance.

## 🎯 What This Application Does

- **Ask Questions**: "Which farms had the highest net farm income?" or "Show me farms with the best debt ratios"
- **AI Analysis**: The application automatically generates SQL queries and provides financial insights
- **Multiple Interfaces**: Web interface, command line, or interactive demo
- **Real-time Data**: Get instant analysis of your farm financial database

## 📋 Prerequisites

Before starting, ensure you have:

- ✅ **Windows 10 or 11** (64-bit)
- ✅ **Git for Windows** installed ([Download here](https://git-scm.com/download/win))
- ✅ **Python 3.8 or higher** installed ([Download here](https://www.python.org/downloads/))
- ✅ **OpenAI API key** ([Get one here](https://platform.openai.com/api-keys))

## 🚀 Step-by-Step Installation

### **Step 0: Prepare Your Files (IMPORTANT!)**

**Before starting, ensure you have ALL these files in the SAME folder:**

```
C:\YourChosenDirectory\
├── user_setup.bat                ← This is what you'll double-click
├── requirements.txt               ← Python dependencies
├── WINDOWS_README.md             ← This instruction file
└── data\                         ← Sample data folder (if included)
    └── samples_v2\               ← CSV sample files
```

**⚠️  CRITICAL: All files must be in the same directory!**

### **Step 1: Install Git for Windows**

1. Download Git from [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Run the installer with default settings
3. Verify installation by opening Command Prompt and typing:
   ```cmd
   git --version
   ```

### **Step 2: Install Python**

1. Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Verify installation by opening Command Prompt and typing:
   ```cmd
   python --version
   ```

### **Step 3: Clone the Project**

1. Open Command Prompt as Administrator
2. Navigate to where you want to install the project (e.g., `C:\Projects\`)
3. Run these commands:
   ```cmd
   cd C:\Projects
   git clone https://github.com/yourusername/ilm_uni.git
   cd ilm_uni
   ```

### **Step 4: Create Virtual Environment**

1. In the project directory, create a virtual environment:
   ```cmd
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```cmd
   venv\Scripts\activate
   ```
   
   **Note**: You should see `(venv)` at the beginning of your command line

### **Step 5: Install Dependencies**

1. With the virtual environment activated, install required packages:
   ```cmd
   pip install -r requirements.txt
   ```

### **Step 6: Get OpenAI API Key**

1. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Click "Create new secret key"
4. Copy the key (it starts with `sk-`)

### **Step 7: Create Environment File**

1. In the project directory, create a file named `.env`
2. Add your OpenAI API key:
   ```env
   OPENAI_API_KEY=sk-your_actual_api_key_here
   DATABASE_PATH=finbin_farm_data.db
   ```

## 🗄️ Database Setup

### **Step 1: Create the Database**

1. Navigate to the `src` folder:
   ```cmd
   cd src
   ```

2. Create the database with sample data:
   ```cmd
   python create_database.py
   ```

3. Verify the database was created:
   ```cmd
   python check_database.py
   ```

   You should see: `✅ Database has data!`

## 🧪 Test Your Installation

### **Quick Test (Recommended First)**

1. Run the quick test to verify everything works:
   ```cmd
   python quick_test.py
   ```

2. Expected output:
   ```
   🌾 Testing Farm Financial RAG Application
   ==========================================
   ✅ Database connection successful
   ✅ Database has data (XX rows)
   ✅ OpenAI API key configured
   ✅ RAG application ready!
   ```

## 🚀 Running the Application

### **Option 0: Simple Setup (Easiest - Recommended)**

**Prerequisites:**
- **Python 3.11 or 3.12** installed ([Download here](https://www.python.org/downloads/))
- **Git** installed ([Download here](https://git-scm.com/download/win))
- **OpenAI API key** ([Get one here](https://platform.openai.com/api-keys))

1. **Ensure all files are in the same folder** (see Step 0 above)
2. **Double-click `user_setup.bat`**
3. **Follow the prompts!** 🪄

**What happens automatically:**
- ✅ **Sets up Python virtual environment**
- ✅ **Installs Python dependencies**
- ✅ **Creates database** with sample data
- ✅ **Launches web interface** automatically in your browser

**Why this approach is simple:**
- 🚫 **No Administrator privileges required**
- 🔒 **User-level installation** - safer and more secure
- 🎯 **Single setup file** - no confusion about which one to use
- 🏢 **Corporate-friendly** - works in restricted environments
- 🚀 **Simple and reliable** - just run the application
- 🌐 **Opens in browser** - no command line knowledge needed

### **Option 1: Interactive Demo (Best for Beginners)**

### **Option 1: Interactive Demo (Best for Beginners)**

1. Run the interactive demo:
   ```cmd
   python demo.py
   ```

2. Choose option 1 for automated demo
3. Watch as the application answers sample questions

### **Option 2: Web Interface (Most User-Friendly)**

1. Start the web server:
   ```cmd
   python farm_rag_api.py
   ```

2. Open your web browser
3. Go to: [http://localhost:8000/web_interface.html](http://localhost:8000/web_interface.html)
4. Type your questions in the text box

### **Option 3: Command Line Interface**

1. Run the CLI version:
   ```cmd
   python farm_rag_app.py
   ```

2. Type your questions directly in the command line

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

## 🔧 Troubleshooting Common Issues

### **Issue: "python is not recognized"**
**Solution**: 
1. Reinstall Python and check "Add Python to PATH"
2. Restart Command Prompt after installation

### **Issue: "pip is not recognized"**
**Solution**:
1. Ensure Python is in PATH
2. Try: `python -m pip install -r requirements.txt`

### **Issue: "No module named 'openai'**
**Solution**:
1. Make sure virtual environment is activated (`venv\Scripts\activate`)
2. Run: `pip install -r requirements.txt`

### **Issue: "Database file not found"**
**Solution**:
1. Navigate to `src` folder: `cd src`
2. Run: `python create_database.py`

### **Issue: "OpenAI API key not configured"**
**Solution**:
1. Check `.env` file exists in project root
2. Ensure API key starts with `sk-`
3. Restart Command Prompt after creating `.env`

### **Issue: "Port 8000 already in use"**
**Solution**:
1. Close other applications using port 8000
2. Or change port in `farm_rag_api.py`

### **Issue: "setup_and_run.ps1 not found" or "requirements.txt not found"**
**Solution**:
1. **Ensure all files are in the same folder** (see Step 0 above)
2. **Don't run from Desktop or Downloads** - create a dedicated folder
3. **Check file names** - they must match exactly:
   - `RUN_ME.bat`
   - `setup_and_run.ps1`
   - `requirements.txt`
4. **Move all files to the same directory** before running

### **Issue: "Cannot find the specified path"**
**Solution**:
1. **Create a dedicated folder** (e.g., `C:\FarmRAG\`)
2. **Copy ALL files** to that folder
3. **Run `RUN_ME.bat` from that folder**
4. **Don't run from network drives or cloud sync folders**

## 📁 File Structure (Windows)

### **Setup Files (What You Need to Download):**
```
C:\YourChosenDirectory\
├── user_setup.bat                # 🚀 MAIN SETUP FILE - Double-click this!
├── requirements.txt               # Python dependencies
├── WINDOWS_README.md             # This instruction file
└── data\                         # Sample data folder (if included)
    └── samples_v2\               # CSV sample files
```

### **After Running Setup (What Gets Created):**
```
C:\Users\YourUsername\FarmRAG\ilm_uni\
├── src\
│   ├── create_database.py        # Database creation script
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
├── venv\                         # Python virtual environment
├── .env                          # Environment configuration
└── FINBIN Data Dictionary Farm.xlsx  # Data dictionary
```

## 🔄 Daily Usage

### **Starting the Application Each Time:**

#### **Option 1: Use the Setup File (Easiest - Recommended)**
1. **Navigate to**: `C:\Users\YourUsername\FarmRAG\ilm_uni\`
2. **Double-click**: `user_setup.bat`
3. **The application starts automatically** and opens in your browser!

#### **Option 2: Manual Command Line (Advanced Users)**
1. Open Command Prompt
2. Navigate to project: `cd C:\Users\YourUsername\FarmRAG\ilm_uni`
3. Activate environment: `venv\Scripts\activate`
4. Go to src: `cd src`
5. Start web interface: `python farm_rag_api.py`
6. Open browser to [http://localhost:8000/web_interface.html](http://localhost:8000/web_interface.html)

### **Stopping the Application:**

1. In Command Prompt, press `Ctrl + C`
2. Type `Y` to confirm

## 📊 Understanding the Results

When you ask a question, the application will:

1. **Generate SQL**: Automatically create the right database query
2. **Execute Query**: Run it against your farm data
3. **Analyze Results**: Process the financial data
4. **Provide Insights**: Give you intelligent analysis and recommendations

### **Sample Response:**
```
Question: "Which farms had the highest net farm income?"

SQL Generated: SELECT farm_name, net_farm_income FROM farms ORDER BY net_farm_income DESC LIMIT 5;

Analysis: Based on the data, the top 5 farms by net farm income are:
1. Green Valley Corn Farm: $320,000
2. Prairie Wheat Farm: $275,000
3. Central Illinois Grain Farm: $290,000
...

Key Insights:
- The highest performing farms are primarily grain operations
- Average net farm income across top farms: $295,000
- These farms show strong operational efficiency
```

## 🎯 Tips for Best Results

1. **Be Specific**: "Which farms in Minnesota have current ratios above 2.0?" vs "Show me farms"
2. **Use Financial Terms**: "debt-to-equity ratio", "working capital", "net farm income"
3. **Ask for Comparisons**: "Compare the performance of dairy vs grain farms"
4. **Request Insights**: "What insights can you provide about farm profitability trends?"

## 🔒 Security Notes

- Keep your OpenAI API key secure
- The database contains sample data only
- Don't share your `.env` file
- Consider the application for development/learning purposes

## 📞 Getting Help

### **If Something Goes Wrong:**

1. **Check the troubleshooting section above**
2. **Verify your setup step by step**
3. **Check the main README.md for more details**
4. **Ensure all prerequisites are installed**

### **Common Windows-Specific Issues:**

- **Path Issues**: Always use `venv\Scripts\activate` (not `source venv/bin/activate`)
- **File Permissions**: Run Command Prompt as Administrator if needed
- **Antivirus**: Some antivirus software may block Python scripts
- **Windows Defender**: May need to allow Python through firewall

## 🚀 Next Steps

After successful installation:

1. **Explore the demo**: `python demo.py`
2. **Try the web interface**: `python farm_rag_api.py`
3. **Ask your own questions** about farm financial data
4. **Customize the application** for your specific needs

## 📚 Learning Resources

- **OpenAI Documentation**: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- **Python Tutorial**: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- **SQL Basics**: [https://www.w3schools.com/sql/](https://www.w3schools.com/sql/)

---

**🎉 Congratulations! You've successfully installed the Farm Financial Data RAG Application on Windows!**

Now you can start asking intelligent questions about farm financial data and get AI-powered insights. Start with the demo to see what's possible, then explore with your own questions!

**Happy Farming! 🌾✨**
