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
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from textblob import TextBlob

#CLEANED_CSV = "data\cleaned\sustainability_submissions_cleaned.csv"
#CLEANED_JSON = "data\cleaned\sustainability_submissions_cleaned.csv"

DESIRED_COLUMNS = [
        "created_utc",
        "title",
        "is_self",
        "selftext",

        "score",
        "ups",
        "downs",

#        "author",
        "num_comments",
#        "num_crossposts",
#        "link_flair_richtext",
        "link_flair_text",
        "subreddit",
        "category",

#        "hidden",
#        "hide_score",
    ]

def time_conversion(timestamp):
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def get_sentiment(input):
    blob = TextBlob(input)

    return (blob.sentiment.polarity, blob.sentiment.subjectivity)


def conversion(input, output):

    print(f"Converting JSON to CSV and filtering columns...")

    df = pd.read_json(input, lines=True)

    pre_len = df.shape


    df = df[DESIRED_COLUMNS]
    df.replace(r"\n"," ",inplace=True, regex=True)
    df.replace(r"\r"," ",inplace=True, regex=True)

    df.dropna(subset=["title","created_utc"])

    # FILTER CRITERIA:
    # - No Self-Text, OR
    # - No Comments, OR
    # - Post has been deleted by User
    df = df[(df["is_self"] == True) | 
            (df["num_comments"] > 0)
#              | 
            ]
    df = df[(df["title"] != "[deleted by user]")]

    post_len = df.shape
    delta_shape = (pre_len[0] - post_len[0],pre_len[1] - post_len[1])
    print(f"Filtered Data; \n CSV Shape comparison: {pre_len} reduced to {post_len};\n delta: {delta_shape}")

    print("Converting Timestamp...")
    df["timestamp"] = df["created_utc"].apply(time_conversion)

    print("Calculating Sentiment of Titles and Text...")
    title_sentiments = df["title"].apply(get_sentiment)
    df[["title_polarity","title_subjectivity"]] = title_sentiments.tolist()

    text_sentiments = df["selftext"].apply(get_sentiment)
    df[["text_polarity","text_subjectivity"]] = text_sentiments.tolist()

    df.sort_values(by=["timestamp","score"])

    print(df.describe(include="all"))
    print(df[["timestamp","title"]].head(20))



    df.to_csv(output)
    print(f"Converted JSON to CSV, Filepath: {output}")

#    plot_posts(df)

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

    for i,col in enumerate(df.columns):

        colsep = col.split(":")


        if colsep[0] in desired_cols:
            print(colsep[0], "||", colsep[1])




def plot_posts(df):

    print("Plotting Text Posts")

    df["smoothed_pol"] = df["text_polarity"].rolling(window=30, center=True).mean()
    df["smoothed_sub"] = df["text_subjectivity"].rolling(window=30, center=True).mean()
    df.index = pd.to_datetime(df.timestamp)

    # Plot for Polarity
    plt.figure(figsize=(15, 10))  # Set the figure size
    plt.plot(df.index, df["smoothed_pol"], label="Polarity", color="blue", marker = None, markersize = 2, alpha = 0.5)
    plt.title("Polarity Analysis Over Time (2016 - Latest)")
    plt.xlabel("Date")
    plt.ylabel("Polarity Score")
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("post_polarity.png")

    # Plot for Subjectivity
    plt.figure(figsize=(15, 10))  # Set the figure size
    plt.plot(df.index, df["smoothed_sub"], label="Subjectivity", color="green", marker = None, markersize = 2, alpha = 0.5)
    plt.title("Subjectivity Analysis Over Time (2016 - Latest)")
    plt.xlabel("Date")
    plt.ylabel("Subjectivity Score")
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("post_subjectivity.png")


def merge_posts_and_comments(df_posts,dfcomments,output):

    df_new = pd.DataFrame(data={
        "Date": pd.to_datetime(df_posts.timestamp),
        "Text": df_posts.title + " | " + df_posts.selftext,
        "Polarity": (df_posts.title_polarity + df_posts.text_polarity) * 0.5,
        "Subjectivity": (df_posts.title_subjectivity + df_posts.text_subjectivity) * 0.5,
    })


    df_merged = pd.merge(dfcomments, df_new, on="Date", how="inner").to_csv(output, index=False)

    return df_merged





    