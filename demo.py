from insurance.pipeline.pipeline import Pipeline
from insurance.exception import InsuranceException
from insurance.logger import logging
from insurance.config.configuration import Configuartion
from insurance.component.data_transformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))

        pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()
