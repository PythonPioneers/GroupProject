# GroupProject

Sentiment Analysis Feedback from Reviews

## Components

Our group project has three stages done asynchronically. Each stage decides the next, as follows:
1. Web scraping: reviews were scraped from Amazon products.
2. Data processing and Model building: the reviews data were preprocessed into trainable/testable data to feed into a model. We tried different hyperparameters to tune up the models until we had a good evaluation score.
3. User Interface: integrating the pre-trained model from step 2 we build a UI that take input of a review and gives instant feedback about sentiment of that review

## 1. Web Scraping

We used Python packages requests_html and pandas to extract data from HTML pages into a .csv file with the following details:

- Title: Title of Review
- Rating: Rating of Review from 1-5
- Comment: Body of the User Review
- asin_number: Amazon Standard Identification Number (unique product code)

extractReviews.py scrapes 300 unique products on Amazon and extracts roughly 3,000 user reviews (10 per product) into reviews.csv. Additionally, we append roughly 5,000 more user reviews from more_reviews.csv (https://www.kaggle.com/datasets/tarkkaanko/amazon?select=amazon_reviews.csv) into the main review csv. 

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

