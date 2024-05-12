import sys
from os.path import basename, splitext, join, dirname

# Add the directories containing the custom modules to the path
sys.path.append(join(dirname(__file__), "data_cleanup"))
sys.path.append(join(dirname(__file__), "processing"))

import data_cleanup.tojson as tojson
import data_cleanup.decompresser as decompresser
import processing.getdata as getdata
import processing.basic_nlp as basic_nlp
import processing.basic_processing as basic_proc

# *** ONLY CHANGE THIS ***
ZST_NAME = "theworldnews_comments.zst"
ZST_NAME = "theworldnews_submissions.zst"
# *** ONLY CHANGE THIS ***
PROCESS_ONLY = False

def main():
    # Set up a base directory relative to the script location
    base_dir = dirname(__file__)

    is_subm = ("submissions" in ZST_NAME)


    # Define file paths relative to base_dir
    zst_file = join(base_dir, "raw data", "raw", ZST_NAME)
    json_file = join(base_dir, "cleaned jsons", "cleaned", f"{splitext(basename(zst_file))[0]}_cleaned.jsonl")
    csv_file = join(base_dir, "cleaned csvs", "cleaned", f"{splitext(basename(zst_file))[0]}_decomp.csv")


    if (is_subm):
        ### CSV Conversion of Submissions
        n_csv_file = join(base_dir, "cleaned jsons", "cleaned", f"{splitext(basename(zst_file))[0]}_csv_cleaned.csv")

        if not PROCESS_ONLY:
            decompresser.tocsv(zst_file, csv_file)
            tojson.tojson(zst_file, json_file)

        basic_proc.conversion(json_file, n_csv_file)
        

    else:
        ### JSON Conversion of Posts
        tojson.tojson(zst_file, json_file)
    
        json_path_pretty = join(base_dir, "raw data", "pretty jsons", f"{splitext(basename(json_file))[0]}_pretty.json")
        getdata.transform(json_file, json_path_pretty)

        in_sentiment = json_path_pretty
        out_path_sentiment = join(base_dir, "sentiment", f"sentiment_{splitext(basename(in_sentiment))[0]}.json")
        
        basic_nlp.sentiment_analysis(in_sentiment, out_path_sentiment)

    print("All processes have been completed.")

if __name__ == "__main__":
    main()

