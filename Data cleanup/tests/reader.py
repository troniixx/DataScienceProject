import pandas as pd

CLEANED_FILE = "data/cleaned/Switzerland_comments_cleaned.csv"

df_pandas = pd.read_csv(CLEANED_FILE, skip_blank_lines=True, on_bad_lines = "skip")
df_pandas = df_pandas.dropna()

print(df_pandas.describe())
print(df_pandas.head())