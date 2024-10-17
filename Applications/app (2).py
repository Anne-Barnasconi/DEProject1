import os
from flask import Flask, request
from baseball_predictor import BaseballPredictor  # Assuming you have a class for baseball predictions

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/baseball_predictor/', methods=['POST'])  # Changed the endpoint
def predict_team():
    # Get the prediction input data from the message body as a JSON payload
    prediction_input = request.get_json()
    
    # Pass the input data to the BaseballPredictor and return the prediction result
    return bp.predict_team_performance(prediction_input)


bp = BaseballPredictor()  # Instantiate the BaseballPredictor class

# The code within this conditional block will only run if the script is executed directly
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
