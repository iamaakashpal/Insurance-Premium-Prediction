from insurance.entity.config_entity import DataIngestionConfig
from insurance.exception import InsuranceException
from insurance.util.util import read_yaml_file
import os,sys
from insurance.logger import logging

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise InsuranceException(e,sys) 

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise InsuranceException(e,sys) from e