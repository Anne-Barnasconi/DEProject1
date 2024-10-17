# Importing Flask and other modules
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
        # Extracting form data submitted by the user
        on_base_percentage = float(request.form.get("on_base_percentage"))
        slugging_percentage = float(request.form.get("slugging_percentage"))
        batting_average = float(request.form.get("batting_average"))
        opponent_on_base_percentage = float(request.form.get("opponent_on_base_percentage"))
        opponent_slugging_percentage = float(request.form.get("opponent_slugging_percentage"))




        ####### MODEL??????? ########
        # we will replace this simple (and inaccurate logic) with a prediction from a machine learning model in a
        # future in a future lab
        if pgc > 120:
            prediction_value = True
        else:
            prediction_value = False

        return render_template("response_page.html",
                               prediction_variable=prediction_value)

    else:
        return jsonify(message="Method Not Allowed"), 405  # The 405 Method Not Allowed should be used to indicate
    # that our app that does not allow the users to perform any other HTTP method (e.g., PUT and  DELETE) for
    # '/checkdiabetes' path


# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
