import random
from datetime import datetime

def generate_motivational_message(sentiment):
    """
    Generate a motivational message based on the sentiment.
    
    Args:
        sentiment (str): The sentiment category ('Positive', 'Negative', or 'Neutral')
    
    Returns:
        str: A motivational message
    """
    positive_messages = [
        "Keep up the positive energy! It's contagious!",
        "Your positive outlook brightens everyone's day!",
        "Wonderful! Positivity leads to possibilities!",
        "That's the spirit! Keep embracing the good vibes!",
        "Fantastic! Your positive energy is your superpower!"
    ]
    
    negative_messages = [
        "Remember, every cloud has a silver lining. Tomorrow is a new day!",
        "It's okay to feel down sometimes. Be kind to yourself today.",
        "Difficult times often lead to the greatest personal growth.",
        "Your feelings are valid. Take the time you need to process them.",
        "This too shall pass. You've overcome challenges before!"
    ]
    
    neutral_messages = [
        "Balance is key. You're doing great!",
        "Steady and calm - that's a good approach to life!",
        "Sometimes neutral is exactly what we need. Keep going!",
        "A balanced mind leads to balanced decisions. You're on the right track!",
        "Mindfulness and awareness - you're practicing important skills!"
    ]
    
    if sentiment == "Positive":
        return random.choice(positive_messages)
    elif sentiment == "Negative":
        return random.choice(negative_messages)
    else:  # Neutral
        return random.choice(neutral_messages)

def truncate_text(text, max_length=50):
    """
    Truncate text to a specified maximum length and add ellipsis if needed.
    
    Args:
        text (str): The text to truncate
        max_length (int): Maximum length before truncation
    
    Returns:
        str: Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def format_date(date_str):
    """
    Format a date string for display.
    
    Args:
        date_str (str): Date string in format 'YYYY-MM-DD HH:MM:SS'
    
    Returns:
        str: Formatted date string
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return date_obj.strftime('%b %d, %Y at %I:%M %p')
    except:
        return date_str
