import polars as pl
import pandas as pd

AUP = "data/cleaned/AmongUsPorn_submissions_cleaned.csv" # AmongUsPorn Data set with 1.5M data points

df = pl.read_csv(AUP, truncate_ragged_lines=True, ignore_errors=True)
df = df.drop_nulls()

# TAKES A VERY LONG TIME - BE PATIENT

print(df.describe())
#print(df.summary())