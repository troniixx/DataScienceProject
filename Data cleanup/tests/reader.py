import pandas as pd

CLEANED_FILE = "data/cleaned/AmongUsPorn_submissions_cleaned.csv"

df_pandas = pd.read_csv(CLEANED_FILE, skip_blank_lines=True, error_bad_lines=False, warn_bad_lines=False)
df_pandas = df_pandas.dropna()

print(df_pandas.describe())
print(df_pandas.head())