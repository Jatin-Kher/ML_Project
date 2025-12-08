from src.MLproject.logger import logging 
from src.MLproject.exception import CustomException
from src.MLproject.components.data_ingestion import DataIngestion
from src.MLproject.components.data_transformation import DataTransformationConfig, DataTransformation

import sys


if __name__ == "__main__": 
    logging.info("the execution has statrted")
    
    try:
        # #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        
        # data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        
        data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        
        
        
    except Exception as e:
        logging.info("dividing by zero is not allowed")
        raise CustomException(e,sys) 