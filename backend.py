from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

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
        print(id, comment, rating, title)
        return data
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
