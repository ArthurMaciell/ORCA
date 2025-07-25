import pandas as pd
import os
from ORCA import logger
from sklearn.linear_model import ElasticNet
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools import add_constant
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import make_scorer, mean_absolute_error
from sklearn.model_selection import cross_val_score
import optuna
from ORCA.entity.config_entity import ModelTrainerConfig



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_excel(self.config.train_data_path)
        test_data = pd.read_excel(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]
        y_train_log = np.log1p(train_y)
        y_test_log = np.log1p(test_y)

        model = XGBRegressor(
            learning_rate=self.config.learning_rate,
            max_depth=5,
            n_estimators=self.config.n_estimators,
            subsample=0.8,
            colsample_bytree=1,
            colsample_bynode=0.75,
            gamma=0,
            min_child_weight=1,
            reg_alpha=0.1,
            reg_lambda=1,
            objective='reg:squarederror'
        )
        model.fit(train_x, y_train_log)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

