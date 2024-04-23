# TODOs


### Process

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




