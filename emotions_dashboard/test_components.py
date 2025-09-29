import os
import sys

def test_all_components():
    results = []
    
    # Test 1: Import all modules
    try:
        import app
        import database
        import sentiment
        import utils
        results.append("✅ All modules imported successfully")
    except Exception as e:
        results.append(f"❌ Module import error: {str(e)}")
    
    # Test 2: Initialize database
    try:
        from database import initialize_db
        initialize_db()
        db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
        if os.path.exists(db_path):
            results.append(f"✅ Database initialized successfully at {db_path}")
        else:
            results.append(f"❌ Database file not created at {db_path}")
    except Exception as e:
        results.append(f"❌ Database initialization error: {str(e)}")
    
    # Test 3: Test sentiment analysis
    try:
        from sentiment import analyze_sentiment
        sentiment_category, sentiment_score = analyze_sentiment("I am feeling great today!")
        results.append(f"✅ Sentiment analysis works: '{sentiment_category}' with score {sentiment_score}")
    except Exception as e:
        results.append(f"❌ Sentiment analysis error: {str(e)}")
    
    # Test 4: Test utils functions
    try:
        from utils import generate_motivational_message, format_date
        message = generate_motivational_message("Positive")
        formatted_date = format_date("2023-05-01 14:30:00")
        results.append(f"✅ Utils functions work: Generated message and formatted date '{formatted_date}'")
    except Exception as e:
        results.append(f"❌ Utils functions error: {str(e)}")
    
    # Print results directly
    for result in results:
        print(result)

if __name__ == "__main__":
    test_all_components()
