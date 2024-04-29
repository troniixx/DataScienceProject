import json
from os.path import basename, splitext
from datetime import datetime, timezone

JSON_PATH = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/data/pretty jsons/Switzerland_comments_pretty.json"
OUT_PATH = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/json_files/cleaned/{splitext(basename(JSON_PATH))[0]}_cleaned.json"

def transform(json_path, out_path):
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    comment_date = {}
    
    for item in data:
        timestamp = int(item["created_utc"])  # Ensure the timestamp is an integer
        readable_date = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        
        # Store the body of the comment with the readable date as the key
        comment_date[readable_date] = item["body"].replace("\\'", "'").replace('\\"', '"')
    
    with open(out_path, "w", encoding="utf-8") as output_file:
        json.dump(comment_date, output_file, indent=4)
    
    return comment_date

if __name__ == "__main__":
    transformed_data = transform(JSON_PATH, OUT_PATH)
    print("Transformed data has been saved to:", OUT_PATH)