import os
import sys
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

# Set up output file
output_file = open("test_results.log", "w")

def log(message):
    """Write message to both console and log file"""
    print(message)
    output_file.write(message + "\n")

log("=== COMPREHENSIVE TEST OF EMOTIONS DASHBOARD ===")
log(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
log("=" * 50)

# Test 1: Import all modules
log("\n1. TESTING MODULE IMPORTS")
try:
    log("Importing app module...")
    import app
    log("✅ App module imported successfully")
except Exception as e:
    log(f"❌ App module import error: {str(e)}")

try:
    log("Importing database module...")
    import database
    log("✅ Database module imported successfully")
except Exception as e:
    log(f"❌ Database module import error: {str(e)}")

try:
    log("Importing sentiment module...")
    import sentiment
    log("✅ Sentiment module imported successfully")
except Exception as e:
    log(f"❌ Sentiment module import error: {str(e)}")

try:
    log("Importing utils module...")
    import utils
    log("✅ Utils module imported successfully")
except Exception as e:
    log(f"❌ Utils module import error: {str(e)}")

# Test 2: Database initialization and operations
log("\n2. TESTING DATABASE OPERATIONS")
try:
    log("Initializing database...")
    database.initialize_db()
    db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
    if os.path.exists(db_path):
        log(f"✅ Database initialized successfully at {db_path}")
    else:
        log(f"❌ Database file not created at {db_path}")
        
    # Test saving an entry
    log("Testing save_entry function...")
    result = database.save_entry("Test emotion entry", "Positive", 0.8)
    if result:
        log("✅ Successfully saved entry to database")
    else:
        log("❌ Failed to save entry to database")
        
    # Test retrieving all entries
    log("Testing get_all_entries function...")
    entries = database.get_all_entries()
    if entries is not None and not entries.empty:
        log(f"✅ Successfully retrieved {len(entries)} entries from database")
    else:
        log("❌ Failed to retrieve entries from database")
        
    # Test retrieving entries by date range
    log("Testing get_entries_by_date_range function...")
    start_date = datetime.now().date() - timedelta(days=7)
    end_date = datetime.now().date()
    date_entries = database.get_entries_by_date_range(start_date, end_date)
    if date_entries is not None:
        log(f"✅ Successfully retrieved {len(date_entries) if not date_entries.empty else 0} entries for date range")
    else:
        log("❌ Failed to retrieve entries by date range")
except Exception as e:
    log(f"❌ Database operations error: {str(e)}")

# Test 3: Sentiment analysis
log("\n3. TESTING SENTIMENT ANALYSIS")
try:
    log("Testing analyze_sentiment function...")
    positive_text = "I am feeling great today!"
    negative_text = "I am feeling terrible today."
    neutral_text = "Today is just another day."
    
    pos_category, pos_score = sentiment.analyze_sentiment(positive_text)
    neg_category, neg_score = sentiment.analyze_sentiment(negative_text)
    neu_category, neu_score = sentiment.analyze_sentiment(neutral_text)
    
    log(f"Positive text analysis: {pos_category} ({pos_score})")
    log(f"Negative text analysis: {neg_category} ({neg_score})")
    log(f"Neutral text analysis: {neu_category} ({neu_score})")
    
    if pos_category == "Positive" and neg_category == "Negative":
        log("✅ Sentiment analysis is working correctly")
    else:
        log("❌ Sentiment analysis results are unexpected")
except Exception as e:
    log(f"❌ Sentiment analysis error: {str(e)}")

# Test 4: Utils functions
log("\n4. TESTING UTILITY FUNCTIONS")
try:
    log("Testing generate_motivational_message function...")
    pos_message = utils.generate_motivational_message("Positive")
    neg_message = utils.generate_motivational_message("Negative")
    neu_message = utils.generate_motivational_message("Neutral")
    
    log(f"Positive message: {pos_message}")
    log(f"Negative message: {neg_message}")
    log(f"Neutral message: {neu_message}")
    
    if pos_message and neg_message and neu_message:
        log("✅ Motivational message generation is working correctly")
    else:
        log("❌ Motivational message generation failed")
        
    log("Testing truncate_text function...")
    long_text = "This is a very long text that should be truncated by the function"
    truncated = utils.truncate_text(long_text, 20)
    if truncated == "This is a very long..." and len(truncated) <= 23:
        log("✅ Text truncation is working correctly")
    else:
        log(f"❌ Text truncation failed: {truncated}")
        
    log("Testing format_date function...")
    date_str = "2023-05-01 14:30:00"
    formatted = utils.format_date(date_str)
    if "May 01, 2023" in formatted:
        log("✅ Date formatting is working correctly")
    else:
        log(f"❌ Date formatting failed: {formatted}")
except Exception as e:
    log(f"❌ Utils functions error: {str(e)}")

# Summary
log("\n" + "=" * 50)
log("TEST SUMMARY")
log("=" * 50)
log("All tests completed. Check the log for any errors.")
log(f"Test finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Close the output file
output_file.close()
log("Test results saved to test_results.log")
