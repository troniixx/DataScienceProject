from os.path import basename, splitext

import data_cleanup.tojson as tojson
import processing.getdata as getdata
import processing.basic_nlp as basic_nlp

def main():
    # Define the source file
    zst_file = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/raw data/raw/shavedgirls_comments.zst"
    json_file = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/cleaned jsons/cleaned/{splitext(basename(zst_file))[0]}_cleaned.jsonl"
    tojson.tojson(zst_file, json_file)
    json_path_pretty = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/raw data/pretty jsons/{splitext(basename(json_file))[0]}_pretty.json"
    getdata.transform(json_file, json_path_pretty)
    in_sentiment = json_path_pretty
    out_path_sentiment = f"/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/sentiment/sentiment_{splitext(basename(in_sentiment))[0]}.json"
    basic_nlp.sentiment_analysis(in_sentiment, out_path_sentiment)

    print("All processes have been completed.")

if __name__ == "__main__":
    main()
