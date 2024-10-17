# Importing Flask and other modules
import json
import os
import logging
import requests
from flask import Flask, request, render_template, jsonify

# Flask constructor
app = Flask(__name__)


# A decorator used to associate the URL with a function
@app.route('/submitteams', methods=["GET", "POST"])
def submit_teams():
    if request.method == "GET":
        # Render the input form page (team statistics input)
        return render_template("input_form_page.html")

    elif request.method == "POST":
        # Extracting form data submitted by the user (Baseball statistics)
        try:
            team_stats = {
                "on_base_percentage": float(request.form.get("on_base_percentage")),
                "slugging_percentage": float(request.form.get("slugging_percentage")),
                "batting_average": float(request.form.get("batting_average")),
                "opponent_on_base_percentage": float(request.form.get("opponent_on_base_percentage")),
                "opponent_slugging_percentage": float(request.form.get("opponent_slugging_percentage"))
            }
        except (ValueError, TypeError):
            return jsonify(message="Invalid input data"), 400



        ############## VANAF HIER VERANDEREN ###############

        logging.debug("Prediction input : %s", prediction_input)

        # use requests library to execute the prediction service API by sending an HTTP POST request
        # use an environment variable to find the value of the diabetes prediction API
        # json.dumps() function will convert a subset of Python objects into a json string.
        # json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        predictor_api_url = os.environ['PREDICTOR_API']
        res = requests.post(predictor_api_url, json=json.loads(json.dumps(prediction_input)))

        prediction_value = res.json()['result']
        logging.info("Prediction Output : %s", prediction_value)
        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
