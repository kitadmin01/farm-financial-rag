# 🧪 Testing the Farm Financial Data RAG Application

This document explains how to test all components of the RAG application to ensure everything is working correctly.

## 🚀 Quick Start Testing

### 1. Basic Environment Test
```bash
cd src
python quick_test.py
```
This runs a simple 5-step test to verify basic functionality.

### 2. Comprehensive Testing
```bash
cd src
python test_rag_app.py
```
This runs all 10 comprehensive tests including performance testing.

### 3. Interactive Demo
```bash
cd src
python demo.py
```
Choose between automated demo or interactive question-asking mode.

## 📋 Test Scripts Overview

| Script | Purpose | Duration | Use Case |
|--------|---------|----------|----------|
| `quick_test.py` | Basic functionality | ~30 seconds | Initial setup verification |
| `test_rag_app.py` | Comprehensive testing | ~2-5 minutes | Full system validation |
| `demo.py` | Showcase functionality | ~1-3 minutes | Demonstrating capabilities |
| `test_setup.py` | Setup verification | ~1 minute | Environment validation |

## 🔧 What Each Test Covers

### Quick Test (`quick_test.py`)
1. ✅ Environment configuration
2. ✅ Database existence
3. ✅ RAG application import
4. ✅ RAG instance creation
5. ✅ Simple question processing

### Comprehensive Test (`test_rag_app.py`)
1. ✅ Environment Configuration
2. ✅ OpenAI API Connection
3. ✅ Database Connection
4. ✅ RAG Application Import
5. ✅ RAG Instance Creation
6. ✅ SQL Generation
7. ✅ SQL Execution
8. ✅ Complete RAG Workflow
9. ✅ API Endpoints
10. ✅ Performance Test

### Demo (`demo.py`)
- Automated demo with 5 sample questions
- Interactive mode for custom questions
- Performance metrics
- Error handling demonstration

## 🎯 Test Scenarios

### Basic Functionality Tests
- **Question Understanding**: Can the LLM understand farm-related questions?
- **SQL Generation**: Does it generate appropriate SQL queries?
- **Database Execution**: Can queries run against the SQLite database?
- **Response Generation**: Does it provide meaningful financial insights?

### Performance Tests
- **Response Time**: How long does each question take?
- **Throughput**: Can it handle multiple questions efficiently?
- **Resource Usage**: Memory and CPU utilization

### Error Handling Tests
- **Invalid Questions**: How does it handle unclear questions?
- **Database Errors**: What happens with malformed SQL?
- **API Failures**: OpenAI API connection issues

## 🚨 Common Test Failures & Solutions

### 1. OpenAI API Key Issues
```
❌ OpenAI API key not configured or invalid format
```
**Solution**: Check your `.env` file and ensure `OPENAI_API_KEY` is set correctly.

### 2. Database Not Found
```
❌ Database file not found: finbin_farm_data.db
```
**Solution**: Run the database creation script first:
```bash
cd src
python create_database.py
```

### 3. Import Errors
```
❌ RAG import error: No module named 'farm_rag_app'
```
**Solution**: Ensure you're in the correct directory and all dependencies are installed:
```bash
pip install -r requirements.txt
```

### 4. OpenAI API Connection Issues
```
❌ OpenAI API error: [Errno 11001] getaddrinfo failed
```
**Solution**: Check internet connection and OpenAI API status.

## 📊 Interpreting Test Results

### All Tests Pass ✅
```
🎉 ALL TESTS PASSED! Your RAG application is fully functional!
```
Your application is ready to use!

### Some Tests Fail ⚠️
```
⚠️  3 test(s) failed. Please review the issues above.
```
Check the specific error messages and use the troubleshooting guide.

### Performance Metrics
- **Response Time**: Should be under 15 seconds for most questions
- **Success Rate**: Should be 100% for basic functionality tests
- **Database Performance**: Queries should execute in under 1 second

## 🔍 Debugging Failed Tests

### Enable Debug Logging
Add this to your Python scripts:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Database Schema
```bash
cd src
sqlite3 finbin_farm_data.db
.schema
.tables
```

### Test OpenAI API Directly
```python
from openai import OpenAI
client = OpenAI(api_key="your_key")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

## 🎮 Interactive Testing

### Ask Custom Questions
Use the interactive demo to test your own questions:
```bash
cd src
python demo.py
# Choose option 2 for interactive mode
```

### Test Specific Scenarios
- **Financial Analysis**: "Which farms are most profitable?"
- **Geographic Queries**: "How does performance vary by state?"
- **Trend Analysis**: "How did metrics change over time?"
- **Benchmarking**: "What are the top 10% performing farms?"

## 📈 Performance Benchmarking

### Expected Performance
- **Simple Queries**: 3-8 seconds
- **Complex Queries**: 8-15 seconds
- **Database Queries**: <1 second
- **OpenAI API Calls**: 2-8 seconds

### Performance Optimization
- Use appropriate model (gpt-3.5-turbo for testing, gpt-4 for production)
- Optimize database queries
- Implement caching for repeated questions
- Monitor API usage and costs

## 🚀 Next Steps After Testing

### If All Tests Pass
1. **Start the API Server**:
   ```bash
   ./start_rag_app.sh
   ```

2. **Use the Web Interface**:
   - Open: http://localhost:8000/web_interface.html

3. **Try the CLI Version**:
   ```bash
   cd src
   python farm_rag_app.py
   ```

### If Tests Fail
1. Review error messages
2. Check the troubleshooting section
3. Verify environment setup
4. Run individual tests to isolate issues

## 📞 Getting Help

### Check These First
1. Environment variables in `.env`
2. Database file existence
3. Python dependencies
4. Internet connectivity
5. OpenAI API key validity

### Common Issues
- **Port conflicts**: Change port in `farm_rag_api.py`
- **Memory issues**: Reduce `MAX_TOKENS` in `.env`
- **API limits**: Check OpenAI usage and billing
- **Database locks**: Ensure no other processes are using the database

## 🎯 Test Checklist

Before running tests, ensure:
- [ ] Virtual environment is activated
- [ ] `.env` file is configured with OpenAI API key
- [ ] Database is created and populated
- [ ] All dependencies are installed
- [ ] No other instances are running
- [ ] Internet connection is available

After tests complete:
- [ ] Review all test results
- [ ] Check performance metrics
- [ ] Verify error handling
- [ ] Test user scenarios
- [ ] Document any issues found

---

**Happy Testing! 🧪✨**

Your RAG application should provide intelligent farm financial analysis once all tests pass.
