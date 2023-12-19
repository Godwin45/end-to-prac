from engineProject import logger
from engineProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from engineProject.pipeline.stage_02_data_cleaning import DataCleaningPipeline

STAGE_NAME = "DAta Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataCleaningPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e