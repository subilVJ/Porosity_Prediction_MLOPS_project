import os
from porosity_pred.constants import *

from dataclasses import dataclass
from datetime import datetime


TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainigPipelineConfig:
    pipline_name:str=PIPELINE_NAME
    artifacts_dir:str=os.path.join(ARTIFACTS,TIMESTAMP)
    timestamp:str=TIMESTAMP

trainig_pipeline_config:TrainigPipelineConfig=TrainigPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir:str=os.path.join(trainig_pipeline_config.artifacts_dir,DATA_INGESTION_DIR_NAME)
    feature_file_path:str=os.path.join(data_ingestion_dir,DATA_INGETSION_FEATURE_STORE_DIR,FILE_NAME)
    train_file_path:str=os.path.join(data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TRAIN_FILE_NAME)
    test_file_path:str=os.path.join(data_ingestion_dir,DATA_INGESTION_INGESTED_DIR,TEST_FILE_NAME)
    train_test_split_ratio:float= DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO