import pandas as pd

CLEANED_CSV = "data/cleaned/PoliticsPeopleTwitter_comments_cleaned.csv"
PRETTY_JSON = "data/pretty jsons/Switzerland_comments_pretty.json"

df = pd.read_json(PRETTY_JSON)

#print(df.describe())
print(df.head())

# get categories of the columns
#print(df.columns)