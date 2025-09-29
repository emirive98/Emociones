#!/usr/bin/env python3
"""
Simple test script to verify core functionality without heavy dependencies
"""

def test_sentiment_basic():
    """Test sentiment analysis with basic TextBlob functionality"""
    try:
        from textblob import TextBlob
        
        # Test positive sentiment
        positive_text = "I am feeling amazing and happy today!"
        blob = TextBlob(positive_text)
        polarity = blob.sentiment.polarity
        
        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
            
        print(f"✅ Sentiment Analysis Test:")
        print(f"   Text: '{positive_text}'")
        print(f"   Sentiment: {sentiment} (Score: {polarity:.2f})")
        
        return True
    except Exception as e:
        print(f"❌ Sentiment Analysis Test Failed: {e}")
        return False

def test_utils_basic():
    """Test utility functions"""
    try:
        import random
        
        # Test motivational message generation (simplified)
        positive_messages = [
            "Keep up the positive energy! It's contagious!",
            "Your positive outlook brightens everyone's day!",
            "Wonderful! Positivity leads to possibilities!"
        ]
        
        message = random.choice(positive_messages)
        print(f"✅ Utils Test:")
        print(f"   Generated message: '{message}'")
        
        return True
    except Exception as e:
        print(f"❌ Utils Test Failed: {e}")
        return False

def test_database_basic():
    """Test basic database operations"""
    try:
        import sqlite3
        import os
        from datetime import datetime
        
        # Create a test database
        db_path = "test_emotions.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS emotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TIMESTAMP NOT NULL,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            sentiment_score REAL NOT NULL
        )
        ''')
        
        # Insert test data
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO emotions (date, text, sentiment, sentiment_score) VALUES (?, ?, ?, ?)",
            (current_time, "Test emotion", "Positive", 0.8)
        )
        
        # Query data
        cursor.execute("SELECT COUNT(*) FROM emotions")
        count = cursor.fetchone()[0]
        
        conn.commit()
        conn.close()
        
        # Clean up
        if os.path.exists(db_path):
            os.remove(db_path)
        
        print(f"✅ Database Test:")
        print(f"   Successfully created table and inserted/queried data")
        print(f"   Record count: {count}")
        
        return True
    except Exception as e:
        print(f"❌ Database Test Failed: {e}")
        return False

def main():
    """Run all basic tests"""
    print("=" * 50)
    print("BASIC FUNCTIONALITY TESTS")
    print("=" * 50)
    
    tests = [
        test_sentiment_basic,
        test_utils_basic,
        test_database_basic
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"RESULTS: {passed}/{total} tests passed")
    print("=" * 50)
    
    if passed == total:
        print("🎉 All basic functionality tests passed!")
        return True
    else:
        print("⚠️  Some tests failed. Check the output above.")
        return False

if __name__ == "__main__":
    main()
