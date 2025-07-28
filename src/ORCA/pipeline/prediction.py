import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        self.columns = joblib.load(Path('artifacts/model_trainer/dummy_columns.pkl'))
        
    def preprocess_input(self, df):
        # Aplica get_dummies no dado novo
        df_encoded = pd.get_dummies(df)

        # Garante que todas as colunas estejam presentes
        for col in self.columns:
            if col not in df_encoded:
                df_encoded[col] = 0

        # Garante a mesma ordem de colunas
        df_encoded = df_encoded[self.columns]

        return df_encoded
    
    def predict(self, data):
        data_preparado = self.preprocess_input(data)
        prediction = self.model.predict(data_preparado)
        
        return prediction
