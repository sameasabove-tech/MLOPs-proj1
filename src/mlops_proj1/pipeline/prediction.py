import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib')) # could be a pickle file here too

    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction