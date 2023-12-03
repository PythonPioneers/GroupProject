from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import nltk 
import joblib

model = joblib.load('/Users/ethanshen/Documents/UIUC/Fa23/CS410/GroupProject/unigram_xgboost_oversample.joblib')
vectorizer = joblib.load('/Users/ethanshen/Documents/UIUC/Fa23/CS410/GroupProject/vectorizer.joblib')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words("english")

app = Flask(__name__)
CORS(app, support_credentials=True)

# IMPORT JOBLIB MODEL HERE

@app.route('/model_change', methods=['POST'])
@cross_origin(supports_credentials=True)


def your_endpoint():
    try:
        data = request.get_json()
        id = data["ID"]
        comment = data["comments"]
        rating = data["Rating"]
        title = data["title"]
        # the data is in a json for one review, and the variables are shown here implement model stuff here
        input_vector = vectorizer.transform([comment])
        prediction = model.predict(input_vector)
        
        # print(id, comment, rating, title)
        return prediction
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
