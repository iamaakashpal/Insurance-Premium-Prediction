from insurance.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,\
ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig


class Configuartion:
    def __init__(self) -> None:
        pass

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        pass