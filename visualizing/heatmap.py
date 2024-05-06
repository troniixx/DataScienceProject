import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DATE_SENT = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/sentiment/sentiment_Switzerland_comments_cleaned_pretty.json"

with open(DATE_SENT, "r") as f:
    data = json.load(f)
    
df = pd.DataFrame(data).T
df.index = pd.to_datetime(df.index)
df = df[df.index >= "2019-01-01"]

pivot_pol = df.pivot_table(index=df.index.month, columns=df.index.year, values="polarity")
pivot_sub = df.pivot_table(index=df.index.month, columns=df.index.year, values="subjectivity")

plt.figure(figsize=(15, 10))
sns.heatmap(pivot_pol, cmap="plasma", vmin = df["polarity"].min(), vmax = df["polarity"].max(), annot=False, fmt=".2f")
plt.title("Polarity Heatmap")
plt.xlabel("Year")
plt.ylabel("Month")
plt.savefig("polarity_heatmap.png")

plt.figure(figsize=(15, 10))
sns.heatmap(pivot_sub, cmap="plasma", vmin = df["subjectivity"].min(), vmax = df["subjectivity"].max(), annot=False, fmt=".2f")
plt.title("Subjectivity Heatmap")
plt.xlabel("Year")
plt.ylabel("Month")
plt.savefig("subjectivity_heatmap.png")