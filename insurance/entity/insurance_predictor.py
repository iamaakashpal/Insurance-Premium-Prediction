import os
import sys

from insurance.exception import InsuranceException
from insurance.util.util import load_object

import pandas as pd


class InsuranceData:

    def __init__(self,
                age : int,
                sex : object,
                bmi : float,
                children :int,
                smoker:object,
                region:object,
                expenses:float=None
                 ):
        try:
            self.age = age
            self.sex = sex
            self.bmi = bmi
            self.children = children
            self.smoker = smoker
            self.region = region
            self.expenses = expenses
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def get_insurance_input_data_frame(self):

        try:
            insurance_input_dict = self.get_insurance_data_as_dict()
            return pd.DataFrame(insurance_input_dict)
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def get_insurance_data_as_dict(self):
        try:
            input_data = {
                "age" : [self.age],
                "sex" : [self.sex],
                "bmi" : [self.bmi],
                "children" :[self.children],
                "smoker":[self.smoker],
                "region":[self.region]
                }
            return input_data
        except Exception as e:
            raise InsuranceException(e, sys) from e


class InsurancePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            if len(folder_name)==0:
                return 0
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir,file_name)
            return latest_model_path
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            expenses = model.predict(X)
            return expenses
        except Exception as e:
            raise InsuranceException(e, sys) from e