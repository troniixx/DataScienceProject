import io
import csv
from tqdm import tqdm
import zstandard as zstd

ZST_FILE = "data/raw/AmongUsPorn_submissions.zst"
OUTPUT_PATH = "data/cleaned/AmongUsPorn_submissions_cleaned.csv"

with open(ZST_FILE, 'rb') as compressed:
    dctx = zstd.ZstdDecompressor()
    with dctx.stream_reader(compressed) as reader:
        text_stream = io.TextIOWrapper(reader, encoding='utf-8')
        text_stream_wrapped = tqdm(text_stream, desc="Processing lines")
        
        # Open the CSV file in write mode
        with open(OUTPUT_PATH, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            
            # Iterate over lines in the wrapped text_stream
            for line in text_stream_wrapped:
                columns = line.strip().split(',')
                
                # Write the row to the CSV file
                writer.writerow(columns)

print('CSV file has been created.')