import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sqlite3
import os

# Import custom modules
from database import initialize_db, save_entry, get_all_entries, get_entries_by_date_range
from sentiment import analyze_sentiment
from utils import generate_motivational_message

# Set page configuration with dark theme
st.set_page_config(
    page_title="Emotions Dashboard",
    page_icon="😊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for dark mode and styling
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
    }
    .sentiment-positive {
        color: #4CAF50;
        font-weight: bold;
    }
    .sentiment-negative {
        color: #F44336;
        font-weight: bold;
    }
    .sentiment-neutral {
        color: #2196F3;
        font-weight: bold;
    }
    .motivational-message {
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Initialize database
    initialize_db()
    
    # App title
    st.title("Emotions Dashboard")
    st.subheader("Track and visualize your emotional journey")
    
    # Sidebar
    with st.sidebar:
        st.header("Filters & Options")
        
        # Date range filter
        st.subheader("Date Range")
        
        # Get min and max dates from database
        db_path = os.path.join(os.path.dirname(__file__), 'emotions.db')
        conn = sqlite3.connect(db_path)
        try:
            df = pd.read_sql_query("SELECT date FROM emotions", conn)
            if not df.empty:
                min_date = pd.to_datetime(df['date']).min().date()
                max_date = pd.to_datetime(df['date']).max().date()
            else:
                min_date = datetime.now().date() - timedelta(days=30)
                max_date = datetime.now().date()
        except:
            min_date = datetime.now().date() - timedelta(days=30)
            max_date = datetime.now().date()
        finally:
            conn.close()
        
        start_date = st.date_input("Start date", min_date)
        end_date = st.date_input("End date", max_date)
        
        # Export options
        st.subheader("Export Options")
        if st.button("Export to CSV"):
            entries = get_all_entries()
            if entries is not None and not entries.empty:
                csv_file = entries.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv_file,
                    file_name="emotions_data.csv",
                    mime="text/csv"
                )
            else:
                st.warning("No data to export")
    
    # Main content area - split into tabs
    tab1, tab2 = st.tabs(["Record Emotion", "Dashboard"])
    
    # Tab 1: Record Emotion
    with tab1:
        st.header("How are you feeling today?")
        
        # Text input for emotion
        emotion_text = st.text_area("Express your feelings", height=150, 
                                    placeholder="Write how you're feeling today...")
        
        # Submit button
        if st.button("Save Entry"):
            if emotion_text.strip():
                # Analyze sentiment
                sentiment_category, sentiment_score = analyze_sentiment(emotion_text)
                
                # Save to database
                save_entry(emotion_text, sentiment_category, sentiment_score)
                
                # Display sentiment result
                sentiment_color = {
                    "Positive": "sentiment-positive",
                    "Negative": "sentiment-negative",
                    "Neutral": "sentiment-neutral"
                }
                
                st.markdown(f"Your emotion has been analyzed as: <span class='{sentiment_color[sentiment_category]}'>{sentiment_category}</span>", 
                            unsafe_allow_html=True)
                
                # Display motivational message
                message = generate_motivational_message(sentiment_category)
                st.markdown(f"<div class='motivational-message'>{message}</div>", unsafe_allow_html=True)
                
                # Clear the input
                st.rerun()
            else:
                st.warning("Please enter some text before submitting")
    
    # Tab 2: Dashboard
    with tab2:
        show_dashboard(start_date, end_date)

def show_dashboard(start_date, end_date):
    """Renders the dashboard visualizations"""
    st.header("Emotions Dashboard")
    
    # Get data filtered by date range
    df = get_entries_by_date_range(start_date, end_date)
    
    if df is None or df.empty:
        st.info("No data available for the selected date range. Start by recording your emotions!")
        return
    
    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Create three columns for the visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sentiment Distribution")
        # Count sentiments
        sentiment_counts = df['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        
        # Create bar chart with Plotly
        fig = px.bar(
            sentiment_counts, 
            x='Sentiment', 
            y='Count',
            color='Sentiment',
            color_discrete_map={
                'Positive': '#4CAF50',
                'Negative': '#F44336',
                'Neutral': '#2196F3'
            },
            text='Count'
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Sentiment Over Time")
        # Group by date and calculate average sentiment score
        daily_sentiment = df.groupby(df['date'].dt.date)['sentiment_score'].mean().reset_index()
        
        # Create line chart with Plotly
        fig = px.line(
            daily_sentiment, 
            x='date', 
            y='sentiment_score',
            markers=True
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            xaxis=dict(showgrid=False, title='Date'),
            yaxis=dict(showgrid=False, title='Sentiment Score')
        )
        # Add a horizontal line at y=0
        fig.add_shape(
            type="line",
            x0=daily_sentiment['date'].min(),
            y0=0,
            x1=daily_sentiment['date'].max(),
            y1=0,
            line=dict(color="gray", width=1, dash="dash")
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Word Cloud
    st.subheader("Word Cloud")
    
    # Combine all text entries
    all_text = " ".join(df['text'].tolist())
    
    if all_text.strip():
        # Generate word cloud
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='#0E1117',
            colormap='viridis',
            max_words=100
        ).generate(all_text)
        
        # Display the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.tight_layout(pad=0)
        st.pyplot(plt)
    else:
        st.info("Not enough text data to generate a word cloud")
    
    # Recent entries
    st.subheader("Recent Entries")
    recent_df = df.sort_values(by='date', ascending=False).head(5)
    
    # Format the dataframe for display
    display_df = recent_df[['date', 'text', 'sentiment']].copy()
    display_df['date'] = display_df['date'].dt.strftime('%Y-%m-%d %H:%M')
    display_df.columns = ['Date', 'Entry', 'Sentiment']
    
    # Apply styling to the dataframe
    def style_sentiment(val):
        color_map = {
            'Positive': 'background-color: rgba(76, 175, 80, 0.2)',
            'Negative': 'background-color: rgba(244, 67, 54, 0.2)',
            'Neutral': 'background-color: rgba(33, 150, 243, 0.2)'
        }
        return color_map.get(val, '')
    
    # Display styled dataframe
    st.dataframe(display_df.style.applymap(style_sentiment, subset=['Sentiment']), use_container_width=True)

if __name__ == "__main__":
    main()
