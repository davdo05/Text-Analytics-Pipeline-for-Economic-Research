#!/usr/bin/env python3

import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ------------------------------------------------------------------
# Download NLTK resources (run once; comment out after first run)
# ------------------------------------------------------------------
# nltk.download('vader_lexicon')
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')

def analyze_sentiment(text: str) -> dict:
    """
    Return polarity scores for the text.
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

def preprocess_text(text: str) -> str:
    """
    Lowercase, tokenize, remove stopwords and non-alphanumeric tokens,
    then return the cleaned text.
    """
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    cleaned = [t for t in tokens if t.isalnum() and t not in stop_words]
    return " ".join(cleaned)

def main():
    # require exactly one argument: the path to your .txt file
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_text_file.txt>")
        sys.exit(1)

    file_path = sys.argv[1]

    # read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    # preprocess & analyze
    cleaned_text = preprocess_text(original_text)
    scores = analyze_sentiment(cleaned_text)

    # only print the sentiment scores
    print("Sentiment Scores:")
    for label, value in scores.items():
        print(f"{label.capitalize()}: {value:.3f}")

if __name__ == "__main__":
    main()