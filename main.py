from src.mlops_proj1 import logger
from src.mlops_proj1.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlops_proj1.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlops_proj1.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlops_proj1.pipeline.stage_04_model_training import ModelTrainerTrainingPipeline


STAGE_NAME_01 = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME_01} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME_02 = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME_02} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME_02} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME_03 = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME_03} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME_03} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME_04 = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME_04} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME_04} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e