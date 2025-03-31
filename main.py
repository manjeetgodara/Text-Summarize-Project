from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import DataModelTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import DataModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation_training_pipeline = DataValidationTrainingPipeline()
    data_validation_training_pipeline.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_transformation_training_pipeline = DataTransformationTrainingPipeline()
    data_transformation_training_pipeline.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    model_training_pipeline = DataModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"Starting {STAGE_NAME}")
    model_evaluation_pipeline = DataModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


