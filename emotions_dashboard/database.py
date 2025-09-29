import sqlite3
import pandas as pd
import os
from datetime import datetime

def initialize_db():
    """
    Initialize the SQLite database and create the emotions table if it doesn't exist.
    """
    db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS emotions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TIMESTAMP NOT NULL,
        text TEXT NOT NULL,
        sentiment TEXT NOT NULL,
        sentiment_score REAL NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

def save_entry(text, sentiment, sentiment_score):
    """
    Save a new emotion entry to the database.
    
    Args:
        text (str): The text describing the emotion
        sentiment (str): The sentiment category (Positive, Negative, Neutral)
        sentiment_score (float): The sentiment polarity score
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get current timestamp
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Insert new entry
        cursor.execute(
            "INSERT INTO emotions (date, text, sentiment, sentiment_score) VALUES (?, ?, ?, ?)",
            (current_time, text, sentiment, sentiment_score)
        )
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error saving entry: {e}")
        return False

def get_all_entries():
    """
    Retrieve all entries from the database.
    
    Returns:
        pandas.DataFrame: DataFrame containing all entries
    """
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
        conn = sqlite3.connect(db_path)
        query = "SELECT * FROM emotions ORDER BY date DESC"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error retrieving entries: {e}")
        return None

def get_entries_by_date_range(start_date, end_date):
    """
    Retrieve entries within a specific date range.
    
    Args:
        start_date (datetime.date): Start date for filtering
        end_date (datetime.date): End date for filtering
    
    Returns:
        pandas.DataFrame: DataFrame containing filtered entries
    """
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
        conn = sqlite3.connect(db_path)
        
        # Convert dates to strings in the format expected by SQLite
        start_date_str = start_date.strftime('%Y-%m-%d 00:00:00')
        end_date_str = end_date.strftime('%Y-%m-%d 23:59:59')
        
        query = """
        SELECT * FROM emotions 
        WHERE date BETWEEN ? AND ?
        ORDER BY date DESC
        """
        
        df = pd.read_sql_query(query, conn, params=(start_date_str, end_date_str))
        conn.close()
        return df
    except Exception as e:
        print(f"Error retrieving entries by date range: {e}")
        return None

def backup_to_csv():
    """
    Backup the database to a CSV file.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        df = get_all_entries()
        if df is not None and not df.empty:
            df.to_csv('emotions_backup.csv', index=False)
            return True
        return False
    except Exception as e:
        print(f"Error backing up to CSV: {e}")
        return False
