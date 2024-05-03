import json
from textblob import TextBlob
from os.path import basename, splitext

"""
Uses the json file gathered from (getdata.py) and performs sentiment analysis on the comments and
stores the sentiment in a new json file.
"""

JSON_CLEAN = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/cleaned jsons/cleaned/Switzerland_comments_pretty_cleaned.json"
OUT_PATH = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/sentiment/sentiment_{splitext(basename(JSON_CLEAN))[0]}.json"

def sentiment_analysis(json_path, output_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    print("Starting sentiment analysis")
    
    sentiment_data = {}
    
    for date, comment in data.items():
        blob = TextBlob(comment)
        sentiment = {'polarity': blob.sentiment.polarity, 'subjectivity': blob.sentiment.subjectivity}
        
        # Store the sentiment with the date as the key
        sentiment_data[date] = sentiment
    
    # Save the sentiment data to the specified output file
    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(sentiment_data, output_file, indent=4)
        
    print(f"Sentiment analysis has been saved to {output_path}")
    
    return sentiment_data

    
# Polarity [-1,1], -1 negative sentiment and 1 positive sentiment.
# Higher Subjectivity [0,1] means that the text contains personal opinion rather than factual information