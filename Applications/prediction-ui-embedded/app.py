# importing Flask and other modules
import json
import logging
import os
from io import StringIO

import pandas as pd
from flask import Flask, request, render_template, jsonify

from baseball_predictor import BaseballPredictor

# Flask constructor
app = Flask(__name__)

dp = BaseballPredictor(os.environ.get('MODEL_NAME', 'MODEL_NAME environment variable is not set.'))


# A decorator used to tell the application
# which URL is associated function
@app.route('/checkbaseball', methods=["GET", "POST"])
def check_baseball():
    if request.method == "GET":
        return render_template("input_form_page.html")

    elif request.method == "POST":
        prediction_input = [
            {
                "On_base_percentage": float(request.form.get("On_base_percentage")),
                "Slugging_percentage": float(request.form.get("Slugging_percentage")),
                "Batting_average": float(request.form.get("Batting_average")),
                "Opponent_on_base_percentage": float(request.form.get("Opponent_on_base_percentage")),
                "Opponent_slugging_percentage": float(request.form.get("Opponent_slugging_percentage"))
            }
        ]
        logging.debug("Prediction Input : %s", prediction_input)
        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        status = dp.predict_single_record(df)

        return render_template("response_page.html",
                               prediction_variable=status[0])

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
