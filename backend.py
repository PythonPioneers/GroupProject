# import flast module
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# instance of flask application
app = Flask(__name__)
CORS(app, support_credentials=True)
 
#IMPORT MODEL HERE FROM JOBLIB

# home route that returns below text when root url is accessed
@app.route('/model_change', methods=['POST'])
@cross_origin(supports_credentials=True)
def your_endpoint():
    try:
        data = request.get_json()
        id = data['ID']
        rating = data['Rating']
        comments = data['comments']
        title = data['title']
        # IMPLEMENT THE PREDICTION HERE BASED ON THE MODEL, IT IS IN A JSON FORMAT, IT CAN BE FED IN ANYWAY EACH ITEM IS ALSO
        # PLACED IN A CERTAIN WAY
        return data

    except Exception as e:
        return jsonify({'error': str(e)}), 500

 
if __name__ == '__main__':  
   app.run()
