# import flask and cors to make sure that the development server will launch when the file is run and can work on Google Chrome
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
# import nltk and joblib to load the saved version of the model that will predict on the comment that is fed in
import nltk 
import joblib

# load the model and vectorizer which will predict and break down the words, also make sure stopwords are known 
model = joblib.load('unigram_xgboost_oversample.joblib')
vectorizer = joblib.load('vectorizer.joblib')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")

# these are headers for the flask methods to make sure the server runs and browser allows 
# for the connection between the frontend and the backend
app = Flask(__name__)
CORS(app, support_credentials=True)

# headers for functions to act as endpoints in the server so that way if the endpoint is called, the function is executed
@app.route('/model_change', methods=['POST'])
@cross_origin(supports_credentials=True)
# function that takes in the comment passed from the review and predicts whether it is positive, negative, or neutral
def model_change():
    try:
        # data is a json that holds the data passed from the frontend
        data = request.get_json()
        # elements of the data json
        comment = data["comments"]
        title = data["title"]
        # the prediction and assignment of sentiment
        input_vector = vectorizer.transform([comment])
        prediction = model.predict(input_vector)
        assert prediction in [0,1,2]
        if prediction == 0:
            return 'Negative'
        elif prediction == 1:
            return 'Neutral'
        elif prediction == 2:
            return 'Positive'
        # returns of the frontend
        return prediction
    # this is there to make sure if there is a problem with the server it will throw an error
    except Exception as e:
        return jsonify({'error': str(e)}), 500
# main function to make sure that the server runs as a server
if __name__ == '__main__':
    app.run(debug=True)
