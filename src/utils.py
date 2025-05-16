import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.logger import logging


from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info(f"Object saved at {file_path}")

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train,X_test,y_test,models,param):
      try:
        report = {}

        for model_name, model in models.items():
            param_grid = param[model_name]

            logging.info(f"--- Processing model: {model_name} ---")
            logging.info(f"Model type: {type(model)}")


            gs = GridSearchCV(model,param_grid,cv=3)
            gs.fit(X_train,y_train)


            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)
            

            y_test_pred = model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_pred)
            logging.info(f"R2 score on test data for {model_name}: {test_model_score}")

            report[model_name] = test_model_score
           
            
        return report

      except Exception as e:
        raise CustomException(e, sys)
      

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)
        logging.info(f"Object loaded from {file_path}")
        return obj
    except Exception as e:
        logging.error(f"Error loading object from {file_path}: {e}")
        raise CustomException(e, sys)

