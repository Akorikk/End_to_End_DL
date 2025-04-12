from CNN.pipeline.stage_1_data_ingestion import DataIngestionTrainingPileline
from CNN import logger


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>{STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPileline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e
    