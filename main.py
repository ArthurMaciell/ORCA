from ORCA import logger
import os
from ORCA.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ORCA.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from ORCA.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from ORCA.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from ORCA.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import os
import mlflow

# Autenticação e configuração do MLflow remoto (DagsHub)
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/ArthurMaciell/ORCA.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "ArthurMaciell"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "9ba42c98aca839c1595d1086f91d6985efa8d261"

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("IA_Orcamento")  # ou outro nome que desejar


if __name__ == '__main__':
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        stage = DataIngestionTrainingPipeline()
        stage.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e