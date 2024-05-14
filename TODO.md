# TODOs


### Process

#### Summary

- Archived Data of Reddit Posts
- Perform Sentiment Analysis on posts
- Analyze Correlation of Data:
  -  Sentiment Data and Real world Events & Topics
  -  Community Rating and Sentiment Data (Overall Community Response)
  -  Trends of Sentiment
- Compare different Communities/Subreddits
  - Response to same topic / in same time frame

#### Step 1
- Clean up Data
	- Relevant Columns of Reddit Posts:
		Title, Text, Upvotes, Downvotes, Date Timestamp
	- Metrics
		- Rating (Upvotes, Downvotes)
		- Comment Quantity
			- Comment rating?
	- Text Data
		- Post Title
		- Post Text Content (if applicable)
		- Post Comments
			- Filter by tree depth, rating rank, etc
- Filter Data
	- First establish pipeline for single Dataset/subreddit
	- Limit Post quantity for initial training
	- Filter to specific topics
		- NLP processing?

#### Step 2
- Use pretrained NLP Model to convert text to numerical data
	- Sentiment Analysis for Sentiment Data
- Convert all data to numerical data
	- Sentiment Analysis on Text

#### Step 3 (optional)

- Train model using new data
- Evaluate Finetune model for optimal results
- Use Model to make predictions
	- e.g. Classification of posts

### Used Methods

#### EDA
Time Series Analysis

#### NLP Model
Use pretrained model
	Potentially, train model with own data

Required Features:
- Sentiment Analysis

### Questions to consider

What NLP Model to use?
    Pattern
    spaCy?

What topics to observe sentiment responses on?
    Covid Quarantine, Starting Early 2020
    ChatGPT and AI, Early 2023
    Controversial Topics
        Celebrity News/Deaths, e.g. Queen Elizabeth Death
        Wars/Conflicts; Russia-Ukraine, Israel-Palestine
    
What data processing can be done?
    EDA on data?
        Time Series Analysis;
    Predictor Model for classificatino?

### ToDO List till Friday (Presi abgab)
- select which subbredits (3-4)
- define Hypothesis
- insert the chosen subreddits data into the code
- get plots
- evaluate the plots
- finish presi
