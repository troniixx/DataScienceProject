import json
from os.path import basename, splitext
from datetime import datetime, timezone

"""
Changes the format of the "prettified" JSON file (tojson.py) to a dictionary with the date as the key and the comment as the value.
--> Removes unnecessary data and changes the timestamp to a readable date.
"""

JSON_PATH = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/data/pretty jsons/Switzerland_comments_pretty.json"
OUT_PATH = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/json_files/cleaned/{splitext(basename(JSON_PATH))[0]}_cleaned.json"

import json
from datetime import datetime, timezone

def transform(json_path, out_path):
    comment_date = {}

    # Read each line as a separate JSON object
    with open(json_path, "r", encoding="utf-8") as file:
        for line in file:
            try:
                item = json.loads(line)  # Load each line as a JSON object
                timestamp = int(item["created_utc"])  # Ensure the timestamp is an integer
                readable_date = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

                # Store the body of the comment with the readable date as the key
                # Handling escape characters specifically for the 'body' text
                comment_body = item["body"].replace("\\'", "'").replace('\\"', '"')
                comment_date[readable_date] = comment_body

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {e}")

    # Write the transformed data to a new JSON file
    with open(out_path, "w", encoding="utf-8") as output_file:
        json.dump(comment_date, output_file, indent=4)

    return comment_date

