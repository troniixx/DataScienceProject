import csv
from tqdm import tqdm
from io import TextIOWrapper
from zstandard import ZstdDecompressor
from os.path import basename, splitext

ZST_FILE = "data/raw/Switzerland_comments.zst" # CHANGE THIS
OUTPUT_PATH = f"data/cleaned/{splitext(basename(ZST_FILE))[0]}_cleaned.csv" # DO NOT CHANGE THIS

with open(ZST_FILE, "rb") as compressed:
    dctx = ZstdDecompressor()
    with dctx.stream_reader(compressed) as reader:
        text_stream = TextIOWrapper(reader, encoding="utf-8")
        text_stream_wrapped = tqdm(text_stream, desc="Processing lines")
        
        # Open the CSV file in write mode
        with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            
            # Iterate over lines in the wrapped text_stream
            for line in text_stream_wrapped:
                columns = line.strip().split(",")
                
                # Write the row to the CSV file
                writer.writerow(columns)

print("CSV file has been created.")