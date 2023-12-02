# GroupProject

Sentiment Analysis Feedback from Reviews

## Components

Our group project has three stages done asynchronically. Each stage decides the next, as follows:
1. Web scraping: reviews were scrapped from Amazon and Youtube websites.
2. Data processing and Model building: the reviews data were preprocessed into trainable/testable data to feed into a model. We tried different hyperparameters to tune up the models until we had a good evaluation score.
3. User Interface: integrating the pre-trained model from step 2 we build a UI that take input of a review and gives instant feedback about sentiment of that review

## 1. Web scraping

We used the Python package beautifulsoup to extract data from HTML pages into .csv files with the following details:

- ID
- Title
- Rating
- Comment
- asin_number (unique asin code)

## 2. Data Mining and Model building

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

### Retraining and re-evaluating
- Repeating the Regression Logistic Classifier and XGBoost for the newly balanced dataset

### Bigram Data Vectorization and 2 Classifiers
- Repeating the above steps but with bigram vectorizations. Tuning hyperparameters along the way.

### Final evaluation and model selection
- Based of confusion matrix table and evalation scores we select the better performing model and download its object.

## 3. User Interface
- Using flask we build our UI and integrate the above model object to process the manual input from user and output the sentiment feedback.

