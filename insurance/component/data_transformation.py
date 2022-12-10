# from cgi import test
from sklearn import preprocessing
from insurance.exception import insuranceException
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