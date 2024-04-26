import json
from tqdm import tqdm
import zstandard as zstd
from os import makedirs
from os.path import basename, splitext

# Replace with the path to your .zst file
ZST_FILE = "data/raw/Switzerland_comments.zst"
JSON_FILE = f"data/cleaned/{splitext(basename(ZST_FILE))[0]}_cleaned.jsonl"  # Changed to .jsonl to represent JSON lines

# Decompress the .zst file without progress bar for file size
with open(ZST_FILE, "rb") as compressed, open(JSON_FILE, "wb") as jsonl_file:
    dctx = zstd.ZstdDecompressor()
    # Decompress the file in chunks
    dctx.copy_stream(compressed, jsonl_file)

print("The .zst file has been decompressed.")

# Assuming each line in the decompressed file is a separate JSON object
json_objects = []
# Obtain the number of lines for the progress bar
num_lines = sum(1 for line in open(JSON_FILE, "r", encoding="utf-8"))

with open(JSON_FILE, "r", encoding="utf-8") as file:
    with tqdm(total=num_lines, desc='Converting to JSON objects') as pbar:
        for line in file:
            try:
                json_object = json.loads(line)
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line} - {e}")
            pbar.update(1)

print("The .zst file has been converted to JSON objects. Starting JSON file generation...")

pretty_json_dir = "data/pretty jsons"
makedirs(pretty_json_dir, exist_ok=True)  # Ensure directory exists
JSON_FILE_PRETTY = f"{pretty_json_dir}/{splitext(basename(ZST_FILE))[0]}_pretty.json"

# Write the list of JSON objects to a JSON file
with open(JSON_FILE_PRETTY, "w", encoding="utf-8") as file:
    json.dump(json_objects, file, indent=4)

print(f"JSON data has been written to {JSON_FILE_PRETTY}")
