import zipfile
from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.entity.config_entity import DataIngestionConfig
from insurance.entity.artifact_entity import DataIngestionArtifact
from insurance.constant import *
import os ,sys
from six.moves import urllib
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig) -> None:
        try:
            logging.info(f"{'+'*20} Data Ingestion Log Started .{'+'*20}")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise InsuranceException(e,sys) from e

    def download_insurance_data(self,) -> str:
        try:
            #extraction remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
            os.makedirs(tgz_download_dir,exist_ok=True)

            insurance_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir, insurance_file_name)

            logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
            urllib.request.urlretrieve(download_url, tgz_file_path)
            logging.info(f"File :[{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path

        except Exception as e:
            raise InsuranceException(e,sys) from e

    def extract_zip_file(self,zip_file_path:str):
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir
            
            if os.path.exists(raw_data_dir):
               os.remove(raw_data_dir)
            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extraction of data started from [{zip_file_path}] into dir :[{raw_data_dir}]")
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)


            logging.info(f"{'*'*20}EXtraction Completed {'*'*20}")

        except Exception as e:
            raise InsuranceException(e,sys) from e

    def split_data_as_train_test(self,)-> DataIngestionArtifact:
        try:
            raw_data_dir=self.data_ingestion_config.raw_data_dir

            file_name=os.listdir(raw_data_dir)[0]

            insurance_file_path=os.path.join(raw_data_dir,file_name)

            insurance_data_frame=pd.read_csv(insurance_file_path)
            
            insurance_data_frame['bmi_category']=pd.cut(insurance_data_frame.bmi,bins=[10,20,30,40,50,np.inf],
                                                    labels=[1,2,3,4,5])
            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
            
            for train_index,test_index in split.split(insurance_data_frame,insurance_data_frame.bmi_category):
                train_dataframe=insurance_data_frame.loc[train_index]
                test_dataframe=insurance_data_frame.loc[test_index]
                train_dataframe=train_dataframe.drop(columns='bmi_category')
                test_dataframe=test_dataframe.drop(columns='bmi_category')

            train_file_path=os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)
            test_file_path=os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)

            if train_dataframe is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                train_dataframe.to_csv(train_file_path,index=False)

            if test_dataframe is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                test_dataframe.to_csv(test_file_path,index=False)

            data_ingestion_artifact=DataIngestionArtifact(train_file_path=train_file_path,
                                                          test_file_path=test_file_path,
                                                          is_ingested=True,
                                                          message=f"Data Ingestion Completed")
            logging.info(f"{'*'*20} Data Ingestion Successfully {'*'*20}")
            return data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e,sys) from e

    def initiate_data_ingestion(self,)->DataIngestionArtifact:
        try:
            zip_file_path=self.download_insurance_data()
            self.extract_zip_file(zip_file_path=zip_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise InsuranceException(e,sys) from e

    def __del__(self):
        logging.info(f"{'#'*20} Data Ingestion Log Completed .{'#'*20} \n\n")


    