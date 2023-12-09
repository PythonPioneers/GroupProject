# Instant Sentimental Analysis Feedback
*This is the final course project for **CS 410 - Text Retrieval & Mining** course at the University of Illinois at Urbana-Champaign. - Fall 2023*

We provide you a tool to give instant sentiment analysis on the submitted review regarding the sentiment levels (Positive, Negative or Neutral).
A marketing or product research personel or department can integrate this tool to develop a batch processing feature that intakes a dataset of reviews and outputs a corresponding list of sentiments. Based on how they analyze this output, it can be beneficial to investigate the overall trend, the outliers, or interesting observation, for further improvements or other decision on the products/services.

**Video Demo Presentation:** <link>

### Project team
- Ethan Shen: ethans11@illinois.edu
- Matt Macrides: mbm12@illinois.edu
- Ajay Ramsunder: ajayr4@illinois.edu
- Huyen Lai: hlai9@illinois.edu

## Background/Problem Statement:
- Technical errors or user mistakes can lead to reviews not matching the ratings given on a product/service.
- Sentimental analysis model can be time consuming to build, and getting proper dataset to train the model can be challenging.
- We also notice a general skewing trend in the positive versus negative or neutral reviews so the get a balanced learning is another challenge.
- It would be useful to have a ready-to-use application that employs a model which has been trained and evaluated at relatively high performance score, to obtain instant sentimental feedback on the given review. Based on this it can open door to developing higher capacity application to batch-process reviews.
  
## System requirements and Usage
### Pre-requisites
- Python/NLP Packages: beautifulsoup,  [NumPy](http://www.numpy.org), [Pandas](https://pandas.pydata.org),
- Logistic Regression model: 
- XGBoost Model:
- Flask:

### Delivery Package 
- The main deliverable of this project is .
- We also have the model building and evaluation steps in the provided python notebooks SentimentAnalysis.ipynb.
- All the project files are contained in the **Group Project** folder and its subfolder of this project
>>- Data folder with crawled reviews from different 
>>- README.md
>>- SentimentAnalysis.ipynb
>>- backend.py
>>- extractReviews.py
>>- unigram_xgboost_oversample.joblib
>>- vectorizer.joblib

### How to use
### Code Walk through

**extractReviews.py**
- Using Python packages requests_html and pandas to extract data from HTML pages into a .csv file with the following details:
>- Title: Title of Review
>- Rating: Rating of Review from 1-5
>- Comment: Body of the User Review
>- asin_number: Amazon Standard Identification Number (unique product code)
- extractReviews.py scrapes 300 unique products on Amazon and extracts roughly 3,000 user reviews (10 per product) into reviews.csv. Additionally, we append roughly 5,000 more user reviews from more_reviews.csv (https://www.kaggle.com/datasets/tarkkaanko/amazon?select=amazon_reviews.csv) into the main review csv. 


**SentimentAnalysis.ipynb**
*** Data Mining and Model Building
Data Preprocessing
- Using panda methods to clean up and remove null data
- Using nltk corpus of stopwords to remove stop words in our data

*** Unigram Data Vectorization
- Using sklearn vectorization packages we convert our data into unigram vector. This sklearn package already includes TF and IDF.
- sklearn also used to split data into train and test sets.

*** Logistic Regression Classifier
- Using sklearn logistic regression classifier object to fit our training data, test on test set, and produce our first evaluation of this classifier.

*** XGBoost Data Feeding and Model Training
- Using Python feature XGBoost to read the data and train with XGB classifier as well evaluation results.

*** Initial Evaluation
- Initial study of evaluation scores and prediction test shows some issue in our data. Because of the nature of online reviews, our data was heavily skewed and thus, resulting in high precision and recall for skewed category (Positive) but very low for the other two categories (Negative and Neutral)
- We explored some resolutions for this skewed data issue: by generating more data while eliminating some positive reviews to balance out data in all categories. Another solution proposed was to oversample the underrepresented categories based off proper IDF approach.

*** Retraining and Re-evaluating
- Repeating the Regression Logistic Classifier and XGBoost for the newly balanced dataset

*** Bigram Data Vectorization and 2 Classifiers
- Repeating the above steps but with bigram vectorizations. Tuning hyperparameters along the way.

*** Final Evaluation and Model Selection
- Based of confusion matrix table and evalation scores we select the better performing model and download its object.

**backend.py**
- blah blah

**unigram_xgboost_oversample.joblib**
- extracted model object

**vectorizer.joblib**
- extracted model vectors

## Team contributions
### Requirement analysis and evaluation of toolkits for this project
- Our team conducted a number of brainstorming sessions to develop a complete idea for our project to meet the group project requirements and also a project feasibility.
- *Dan* proposed & took spaCy toolkit through evaluation for this project implementation and tech review
- *Gassan* proposed & took NLTK toolkit through evaluation for this project implementation and tech review
- *Ved* performed evaluation of MetaPy to complete perspective and ensure the right selection of tool happens based on text mining capabilities suited for the implementation.  
- Based on the output of evaluation & individual POC implementations, spaCy won hands-down due to powerful, scalable features complemented with the machine-learning capabilities for the potential enhancements 

### Dataset selection and preparation
- We selected 25,000 uniform randomly selected e-mails from the entire bank of Enron email corpus
- After data wrangling and cleaning efforts, each of us picked 300 distinct emails for the manual classification of emails into important and unimportant categories for training and evaluation of the classifier
- We chose to utilize the whole set of 25,000 emails for summarization module

### Implementation 
- We collectively selected spaCy implementation of classifier by *Dan* to collaboratively develop upon, mainly due to the simplicity and yet powerful features spaCy offered
- *Ved* manually tested the package of classifier and summarizer through introduction.ipynb as a wrapper and one set of manually categorized 300 emails. Noted and shared the observations with the team.  
- *Gassan* wrote an evaluation module to evaluate the result of classifier to quantitatively measure the accuracy and precision of the classifier
- Testing & evaluation feedback provided inputs for finetuning of classifier and summarizer which *Dan* incorporated into the code

## Potential Enhancements
- Integrate with the Mailbox and show summary of top important emails in specific time period: week/month
- List of important/top contacts based on frequent senders/receivers that has important email content 
- Suggestions on de-registering from distribution lists
- Suggestions on email templates based on common phrases/formats used frequently



Sentiment Analysis Feedback from Reviews

## Components

Our group project has three stages done asynchronically. Each stage decides the next, as follows:
1. Web scraping: reviews were scraped from Amazon products.
2. Data processing and Model building: the reviews data were preprocessed into trainable/testable data to feed into a model. We tried different hyperparameters to tune up the models until we had a good evaluation score.
3. User Interface: integrating the pre-trained model from step 2 we build a UI that take input of a review and gives instant feedback about sentiment of that review

## 1. Web Scraping


## 2. Data Mining and Model Building

### Data Preprocessing
- Using panda methods to clean up and remove null data
- Using nltk corpus of stopwords to remove stop words in our data

### Unigram Data Vectorization
- Using sklearn vectorization packages we convert our data into unigram vector. This sklearn package already includes TF and IDF.
- sklearn also used to split data into train and test sets.

### Logistic Regression Classifier
- Using sklearn logistic regression classifier object to fit our training data, test on test set, and produce our first evaluation of this classifier.

### XGBoost Data Feeding and Model Training
- Using Python feature XGBoost to read the data and train with XGB classifier as well evaluation results.

### Initial Evaluation
- Initial study of evaluation scores and prediction test shows some issue in our data. Because of the nature of online reviews, our data was heavily skewed and thus, resulting in high precision and recall for skewed category (Positive) but very low for the other two categories (Negative and Neutral)
- We explored some resolutions for this skewed data issue: by generating more data while eliminating some positive reviews to balance out data in all categories. Another solution proposed was to oversample the underrepresented categories based off proper IDF approach.

### Retraining and Re-evaluating
- Repeating the Regression Logistic Classifier and XGBoost for the newly balanced dataset

### Bigram Data Vectorization and 2 Classifiers
- Repeating the above steps but with bigram vectorizations. Tuning hyperparameters along the way.

### Final Evaluation and Model Selection
- Based of confusion matrix table and evalation scores we select the better performing model and download its object.

## 3. User Interface
### Frontend

We built a frontend component in ReactJS that allows a user to manually feed in any review and then submit the review to be analyzed by the model

#### Components 
- Form: The form allows a user to submit the review and is the container for the different components on the page
- Labels: Tells the user what to input in which textbox or dropdown element
- Textboxes: These are for the user to input text that will then be passed to the model
- Dropdown: Similar function to the textboxes
- Background Color: This is changed based on the output that the model gives, Positive: Green, Neutral: Yellow, Negative: Red

### Backend 

A backend was built using Flask that allowed for the comment from the frontend to be passed through and analyzed and then the response be sent back to the frontend

#### Endpoints
- /model_change (POST) - This calls the model and sends the user's comment through to determine the sentiment of the comment

