import json
from textblob import TextBlob
from os.path import basename, splitext

JSON_CLEAN = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/cleaned jsons/cleaned/Switzerland_comments_pretty_cleaned.json"

def sentiment_analysis(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    sentiment_data = {}
    
    for date, comment in data.items():
        blob = TextBlob(comment)
        sentiment = blob.sentiment
        
        # Store the sentiment with the date as the key
        sentiment_data[date] = sentiment
    
    return sentiment_data

if __name__ == "__main__":
    sentiment_data = sentiment_analysis(JSON_CLEAN)
    print(sentiment_data)
    
# Polarity [-1,1], -1 negative sentiment and 1 positive sentiment.
# Higher Subjectivity [0,1] means that the text contains personal opinion rather than factual information