"""
PROCESS:
- Filter Data
- Remove Unneeded Columns
- Sort by Time

"""
import pandas as pd
import numpy as np
import tqdm
import json
from datetime import datetime, timezone


CLEANED_CSV = "data\cleaned\sustainability_submissions_cleaned.csv"
CLEANED_JSON = "data\cleaned\sustainability_submissions_cleaned.csv"

DESIRED_COLUMNS = [
        "created_utc",
        "title",
        "is_self",
        "selftext",

        "score",
        "ups",
        "downs",

        "author",
        "num_comments",
        "num_crossposts",
        "link_flair_richtext",
        "link_flair_text",
        "subreddit",
        "category",

        "hidden",
        "hide_score",
    ]

def time_conversion(timestamp):
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def conversion(input, output):

    print(f"Converting JSON to CSV and filtering columns...")

    df = pd.read_json(input, lines=True)

    df = df[DESIRED_COLUMNS]

    print(df.describe(include="all"))

    df["timestamp"] = df["created_utc"].apply(time_conversion)
    df.sort_values(by=["timestamp","score"])


    df.to_csv(output)
    print(f"Converted JSON to CSV, Filepath: {output}")

    return

    print("test")

    ### CODE BELOW IS FOR ANALYZING DATA & READING OUT COLUMNS
    json_objects = []

    # JSON TO CSV
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            try:
                json_object = json.loads(line)
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line} - {e}")


    uniq_set = set()
    key_len = 0
    #LOOP FOR EXTRACTING KEYS
    for item in json_objects:
        for key,val in item.items():
            uniq_set.add(key)
            if len(uniq_set) != key_len:
                key_len = len(uniq_set)
                print("New Key Count:",key_len)

    for key in uniq_set:
        print(key)


def process_csv(input):

    df = pd.read_csv(CLEANED_CSV, skip_blank_lines=True, on_bad_lines = "skip")

    

    head = df.head()
    
    print(head)

    

    for i,col in enumerate(df.columns):

        colsep = col.split(":")


        if colsep[0] in desired_cols:
            print(colsep[0], "||", colsep[1])



#get_columns(CLEANED_CSV)