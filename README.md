# Automated Stock Sentiment Analyzer

This project is an **Automated Stock Sentiment Analyzer** that scrapes finance headlines, analyzes their sentiment, and provides investment recommendations ("Buy," "Sell," or "Hold") based on the sentiment score.



## Technologies Used

- Python
- `requests` for web scraping
- `BeautifulSoup` for HTML parsing
- `NLTK` for natural language processing (VADER for sentiment analysis)

## Features

- Fetches the latest finance headlines from a specified news website
- Analyzes the sentiment of each headline
- Provides actionable investment recommendations based on sentiment scores
- Implements error handling and retry logic for robust performance

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-sentiment-analyzer.git
   cd stock-sentiment-analyzer
