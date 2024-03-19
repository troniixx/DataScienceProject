import polars as pl
import pandas as pd

AUP = "data/cleaned/AmongUsPorn_submissions_cleaned.csv" # AmongUsPorn Data set with 1.5M data points

df_polars = pl.read_csv(AUP, truncate_ragged_lines=True, ignore_errors=True)
df_polars = df_polars.drop_nulls()

df_pandas = pd.read_csv(AUP, skip_blank_lines=True, error_bad_lines=False, warn_bad_lines=False)
df_pandas = df_pandas.dropna()


print(df_polars.describe())
print(df_pandas.summary())