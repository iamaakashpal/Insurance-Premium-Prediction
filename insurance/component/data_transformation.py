from cgi import test
from sklearn import preprocessing
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.entity.config_entity import DataTransformationConfig 
from insurance.entity.artifact_entity import DataIngestionArtifact,\
DataValidationArtifact,DataTransformationArtifact
import sys,os
import numpy as np
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
from insurance.constant import *
from insurance.util.util import read_yaml_file,save_object,save_numpy_array_data,load_data

class DataTransformation:

    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,
                data_validation_artifact:DataValidationArtifact,
                data_transformation_config:DataTransformationConfig):
        try:
            logging.info(f"# {'='*10} # Data Transformation Log Started. # {'='*10} #")
            self.data_transformation_config=data_transformation_config
            self.data_validation_artifact=data_validation_artifact
            self.data_ingestion_artifact=data_ingestion_artifact

        except Exception as e:
            raise InsuranceException(e,sys) from e