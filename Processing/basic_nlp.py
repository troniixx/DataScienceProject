import json
from textblob import TextBlob
from os.path import basename, splitext

JSON_CLEAN = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/cleaned jsons/cleaned/Switzerland_comments_pretty_cleaned.json"
OUT_PATH = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/sentiment/sentiment_{splitext(basename(JSON_CLEAN))[0]}.json"

def sentiment_analysis(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    print("Starting sentiment analysis")
    
    sentiment_data = {}
    
    for date, comment in data.items():
        blob = TextBlob(comment)
        sentiment = blob.sentiment
        
        # Store the sentiment with the date as the key
        sentiment_data[date] = sentiment
    
    with open(f"sentiment_{splitext(basename(json_path))[0]}.json", "w", encoding="utf-8") as output_file:
        json.write("[date: polarity, subjectivity]")
        json.dump(sentiment_data, output_file, indent=4)
        
    print("Sentiment analysis has been saved to a JSON file.")
    
    return sentiment_data

if __name__ == "__main__":
    sentiment_data = sentiment_analysis(JSON_CLEAN)
    
# Polarity [-1,1], -1 negative sentiment and 1 positive sentiment.
# Higher Subjectivity [0,1] means that the text contains personal opinion rather than factual information