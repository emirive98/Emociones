import os
import sys

print("Starting simple test...")

# Test 1: Import all modules
try:
    import app
    print("✅ App module imported successfully")
except Exception as e:
    print(f"❌ App module import error: {str(e)}")

try:
    import database
    print("✅ Database module imported successfully")
except Exception as e:
    print(f"❌ Database module import error: {str(e)}")

try:
    import sentiment
    print("✅ Sentiment module imported successfully")
except Exception as e:
    print(f"❌ Sentiment module import error: {str(e)}")

try:
    import utils
    print("✅ Utils module imported successfully")
except Exception as e:
    print(f"❌ Utils module import error: {str(e)}")

# Test 2: Initialize database
try:
    from database import initialize_db
    initialize_db()
    db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
    if os.path.exists(db_path):
        print(f"✅ Database initialized successfully at {db_path}")
    else:
        print(f"❌ Database file not created at {db_path}")
except Exception as e:
    print(f"❌ Database initialization error: {str(e)}")

print("Simple test completed.")
