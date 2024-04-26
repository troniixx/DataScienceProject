import pandas as pd

CLEANED_FILE = "data/cleaned/PoliticsPeopleTwitter_comments_cleaned.csv"

df = pd.read_csv(CLEANED_FILE, skip_blank_lines=True, on_bad_lines = "skip")
df = df.dropna()

#print(df.describe())
#print(df.head())

# get categories of the columns
print(df.dtypes)