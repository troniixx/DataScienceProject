import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

DATE_SENT = "/Users/merterol/Desktop/UZH/CompLing:CompSci/CompSci/Sem2/ESC403/ESC403_Project/DataScienceProject/sentiment/sentiment_Switzerland_comments_cleaned_pretty.json"

with open(DATE_SENT, "r") as f:
    data = json.load(f)
    
df = pd.DataFrame(data).T
df.index = pd.to_datetime(df.index)
df = df[df.index >= "2019-01-01"]
df["smoothed_pol"] = df["polarity"].rolling(window=30, center=True).mean()
df["smoothed_sub"] = df["subjectivity"].rolling(window=30, center=True).mean()

# Plot for Polarity
plt.figure(figsize=(15, 10))  # Set the figure size
plt.plot(df.index, df["smoothed_pol"], label="Polarity", color="blue", marker = None, markersize = 2, alpha = 0.5)
plt.title("Polarity Analysis Over Time (2016 - Latest)")
plt.xlabel("Date")
plt.ylabel("Polarity Score")
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("polarity.png")

# Plot for Subjectivity
plt.figure(figsize=(15, 10))  # Set the figure size
plt.plot(df.index, df["smoothed_sub"], label="Subjectivity", color="green", marker = None, markersize = 2, alpha = 0.5)
plt.title("Subjectivity Analysis Over Time (2016 - Latest)")
plt.xlabel("Date")
plt.ylabel("Subjectivity Score")
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("subjectivity.png")