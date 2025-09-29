# Emotions Dashboard

A modern, interactive dashboard for tracking and visualizing your emotional journey using sentiment analysis.

## Features

- **Emotion Tracking**: Record your daily emotions with a simple text input
- **Sentiment Analysis**: Automatic classification of emotions as Positive, Negative, or Neutral using TextBlob
- **Data Visualization**: View your emotional trends through interactive charts and a word cloud
- **Data Storage**: All entries are stored in a SQLite database with CSV export option
- **Modern UI**: Clean, minimalist design with dark mode by default

## Screenshots

(Screenshots will appear once the application is running)

## Tech Stack

- **Frontend**: Streamlit - for the interactive UI components
- **Data Analysis**: Pandas - for data manipulation and analysis
- **Sentiment Analysis**: TextBlob - for natural language processing and sentiment analysis
- **Data Storage**: SQLite - for persistent storage of emotion entries
- **Visualization**: Plotly, Matplotlib, WordCloud - for creating interactive charts and visualizations

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd emotions_dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

4. Open your browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

## Project Structure

- `app.py`: Main Streamlit application
- `database.py`: Database operations (SQLite)
- `sentiment.py`: Sentiment analysis functionality
- `utils.py`: Utility functions
- `requirements.txt`: Project dependencies
- `emotions.db`: SQLite database (created on first run)

## Usage

1. **Record an Emotion**:
   - Navigate to the "Record Emotion" tab
   - Enter your thoughts or feelings in the text area
   - Click "Save Entry" to analyze and store your emotion

2. **View Dashboard**:
   - Navigate to the "Dashboard" tab
   - Use the sidebar to filter by date range
   - Explore the visualizations:
     - Sentiment Distribution (bar chart)
     - Sentiment Over Time (line chart)
     - Word Cloud of your most used words
     - Recent Entries table

3. **Export Data**:
   - Use the "Export to CSV" button in the sidebar to download your data

## Future Enhancements

- Multi-user support
- More advanced sentiment analysis
- Additional visualization options
- Emotion tagging system
- Mobile app integration

## License

This project is licensed under the MIT License - see the LICENSE file for details.
