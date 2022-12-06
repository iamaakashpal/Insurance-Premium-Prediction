from insurance.pipeline.pipeline import Pipeline
from insurance.logger import logging
from insurance.exception import InsuranceException

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == '__main__':
    main()