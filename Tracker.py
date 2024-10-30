import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time
import nltk

# Download VADER lexicon
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Function to get finance headlines with retries and error handling
def get_finance_headlines(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    attempts = 3
    for attempt in range(attempts):
        try:
            response = requests.get(url, headers=headers, timeout=10)  # 10-second timeout
            response.raise_for_status()  # Check if the request was successful (200 OK)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Adjust this part based on the actual site structure.
            # Here, we assume headlines are in <h3> tags (e.g., Yahoo Finance)
            headlines = [h3.get_text() for h3 in soup.find_all("h3")]
            return headlines
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5)  # Wait before retrying
    return []

# Function to analyze sentiment of each headline
def analyze_headline_sentiment(headline):
    sentiment_score = sia.polarity_scores(headline)["compound"]
    # Suggestion based on sentiment score
    if sentiment_score >= 0.2:
        return "Buy"
    elif sentiment_score <= -0.2:
        return "Sell"
    else:
        return "Hold"

# Main function to get headlines and provide suggestions
def get_stock_suggestions():
    url = "https://finance.yahoo.com"  # Replace with the actual finance news URL you want to scrape
    headlines = get_finance_headlines(url)
    suggestions = {}

    for headline in headlines:
        suggestion = analyze_headline_sentiment(headline)
        suggestions[headline] = suggestion
    
    return suggestions

# Get suggestions and print them
if __name__ == "__main__":
    stock_suggestions = get_stock_suggestions()
    if stock_suggestions:
        for headline, suggestion in stock_suggestions.items():
            print(f"Headline: {headline}\nSuggestion: {suggestion}\n")
    else:
        print("Failed to retrieve any headlines.")
