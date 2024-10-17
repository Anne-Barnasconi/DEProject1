import json
import os

import pandas as pd
from flask import jsonify
from keras.models import load_model
import logging
from io import StringIO


class BaseballPredictor:
    def __init__(self):
        self.model = None

    def predict_single_record(self, prediction_input):
        logging.debug(prediction_input)
        if self.model is None:
            try:
                model_repo = os.environ['MODEL_REPO']
                file_path = os.path.join(model_repo, "mlp_model_15102024.h5")
                self.model = load_model(file_path)
            except KeyError:
                print("MODEL_REPO is undefined")
                self.model = load_model('mpl_model15102024.h5')

        df = pd.read_json(StringIO(json.dumps(prediction_input)), orient='records')
        y_pred = self.model.predict(df)
        logging.info(f"Prediction: {y_pred[0]}")
        playoff_prediction = int(y_pred[0])  # Ensure it's an integer (0 or 1)

        # Return the binary prediction outcome (1 for 'reach playoffs', 0 for 'not reach playoffs')
        return jsonify({'result': playoff_prediction}), 200
