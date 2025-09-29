from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using TextBlob.
    
    Args:
        text (str): The text to analyze
    
    Returns:
        tuple: (sentiment_category, sentiment_score)
            sentiment_category (str): 'Positive', 'Negative', or 'Neutral'
            sentiment_score (float): The polarity score from -1 (negative) to 1 (positive)
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity score (-1 to 1)
    polarity = blob.sentiment.polarity
    
    # Classify the sentiment based on the polarity score
    if polarity > 0.1:
        sentiment_category = "Positive"
    elif polarity < -0.1:
        sentiment_category = "Negative"
    else:
        sentiment_category = "Neutral"
    
    return sentiment_category, polarity

def get_sentiment_color(sentiment):
    """
    Get the color associated with a sentiment category.
    
    Args:
        sentiment (str): The sentiment category ('Positive', 'Negative', or 'Neutral')
    
    Returns:
        str: Hex color code
    """
    color_map = {
        "Positive": "#4CAF50",  # Green
        "Negative": "#F44336",  # Red
        "Neutral": "#2196F3"    # Blue
    }
    
    return color_map.get(sentiment, "#9E9E9E")  # Default to gray if not found

def get_emoji_for_sentiment(sentiment):
    """
    Get an emoji representing the sentiment.
    
    Args:
        sentiment (str): The sentiment category ('Positive', 'Negative', or 'Neutral')
    
    Returns:
        str: Emoji character
    """
    emoji_map = {
        "Positive": "😊",
        "Negative": "😔",
        "Neutral": "😐"
    }
    
    return emoji_map.get(sentiment, "❓")  # Default to question mark if not found
