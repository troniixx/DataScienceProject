# DataScienceProject

This project performs Sentiment Analysis on user-submitted posts and comments of specific subreddits.

## Data Used

This project uses archives of reddit posts and comments, sourced from "The-Eye" Reddit Archives : https://the-eye.eu/redarcs/
This publicly available archive stores the submissions(posts) and comments for the top 20'000 subreddits, spanning from June 2008 to December 2022.

This archive has compressed .zst files, one for submissions(posts) and one for comments, 
containing JSON objects on each line of the file.


## Pipeline Summary

1. **Decompression:** Subreddit .zst files are decompressed into JSON files. (tojson.py)
2. **Data Cleanup:** Relevant data columns are extracted and Sentiment Analysis is performed on the text content. (basic_nlp.py/basic_processing.py)
3. **Data Merging:** The new datasets for posts and submissions are merged into a single CSV File.
4. **Visualization (visualizer.ipynb):** The dataset is plotted for Exploratory Data Analysis. 
5. **Event Impact Analysis (event_impact.ipynb):** The dataset is analyzed for Trends in sentiment, using:
	- Time Series Analysis (ARIMA)
	- Random Forest
	- SVM (Unused due to lackluster performance)




## Code Files Used

### Data Cleaning

main.py
Serves as a management file for running the data processing pipeline and creating transitionary files of the data.
The ZST_NAME variable determines which file is processed. Depending on whether it contains posts or comments, it is processed slightly differently. The important data transformations (Date and Sentiment Analysis) are the same, with a difference in what data and columns are filtered.

#### Pipeline for Comments

##### tojson.py
Decompresses a .zst file into a JSON file, with each JSON Object stored on a seperate line. The resulting JSON file is saved with the ending "cleaned.jsonl"

##### getdata.py
Transforms a JSON file into a human readable form with only the extracting the Timestamp and Text. The file is saved with the ending "pretty.json"

##### basic_nlp.py
Performs Sentiment Analysis on the Text of comments from a JSON File. This is done using textblob, which returns polarity ([-1,+1]) and subjectivity ([0,1]) scores. These are added to the Timestamp and Text data, and stored in a file named "sentiment_SUBREDDITNAME_comments.json"
	

#### Pipeline for Submissions

##### to_json.py
Performs the same Decompression of .zst into .json as listed above.

##### basic_processing.py
Loads a decompressed JSON File as a Pandas DataFrame, where the relevant columns are selected and then filtered to remove irrelevant data points, such as removed or inactive submissions. Sentiment Analysis using textblob is then performed on the Title and Text of the post.
This new data is then saved as a CSV File, with the ending "csv_cleaned.csv".


### Data Processing & Visualization

##### visualizer.ipynb
This Jupyter Notebook merges the data from the posts and comments, which is saved with the ending "df_merged.csv". This File is the final state of the data set.
Various Distributions and Heatmaps  of the data are plotted for EDA.

##### event_impact.ipynb
The merged CSV file is analyzed for the impact on sentiment of various events. This is done using ARIMA Time Series Analysis of the data and Random Forest Regression. The results are then analyzed for significance of impact and general trends.


