import os 
from datetime import datetime

TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str='test.csv'

MODEL_NAME:str="model.pkl"
PREPROCESSING_OBJECT_FILE_NAME:str="preprocessing.pkl"

ARTIFACTS:str="artifacts"
PIPELINE_NAME:str="porosity"
FILE_NAME:str="porosity_file.xlsx"


'''
DATA INGESTION REALTED CONSTANTS STARTS WITH DATA INGESTION VAR
'''
DATA_INGESTION_COLLECTION_NAME:str="porosity_data"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGETSION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2
