#!/usr/bin/env python3
"""
Test script to verify database creation works properly.
"""

import os
import sys

def test_database_creation():
    """Test the database creation process."""
    
    print("🧪 Testing Database Creation")
    print("=" * 50)
    
    # Check current directory
    print(f"📁 Current directory: {os.getcwd()}")
    
    # Check if we're in the right directory
    if not os.path.exists("create_database.py"):
        print("❌ create_database.py not found in current directory")
        print("Please run this script from the src directory")
        return False
    
    # Check if data directory exists
    data_dir = "../data/samples_v2"
    print(f"🔍 Checking data directory: {os.path.abspath(data_dir)}")
    
    if os.path.exists(data_dir):
        print("✅ Data directory exists")
        files = os.listdir(data_dir)
        print(f"📁 Found {len(files)} files:")
        for file in files:
            print(f"   - {file}")
    else:
        print("❌ Data directory does not exist - will use sample data")
    
    # Run the database creation
    print("\n🚀 Running create_database.py...")
    try:
        import create_database
        create_database.main()
        return True
    except Exception as e:
        print(f"❌ Error running create_database.py: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_database_creation()
    if success:
        print("\n✅ Database creation test completed!")
    else:
        print("\n❌ Database creation test failed!")
        sys.exit(1)

