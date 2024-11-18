import os
import sys
from pandas import DataFrame
import pandas as pd
from sklearn.model_selection import train_test_split

from porosity_pred.exception import PorousException
from porosity_pred.logger import logging
from porosity_pred.entity.artifact_entity import DataIngestionArtifact
from porosity_pred.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_inegestion_config=data_ingestion_config
        except Exception as e:
            raise PorousException(e,sys)

    def split_data_as_train_test(self,dataframe:DataFrame)->None:
        '''
        Method Nme: split data as train test
        describtion: This method will split the data into train and test data
        '''
        logging.info("Entered into method split_data_as_train_test in DataIngestion class")
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_inegestion_config.train_test_split_ratio)
            logging.info("performed train and test split dataframe")
            logging.info("Exited split_data_as_train_test method in DataIngestion class")
            dir_path=os.path.dirname(self.data_inegestion_config.train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("Exporting train and test file path")
            train_set.to_csv(self.data_inegestion_config.train_file_path,index=False,header=True)
            test_set.to_csv(self.data_inegestion_config.test_file_path,index=False,header=True)
        except Exception as e:
            raise PorousException(e,sys)
    
    def intiate_data_ingetsion(self)->DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """

        logging.info("Entered into intiate_data_ingestion_method in DataIngestion class")

        try:
            dataframe=pd.read_excel("notebook/porosity_file.xlsx")
            logging.info("Read the data")
            self.split_data_as_train_test(dataframe)


            data_ingestion_artifact=DataIngestionArtifact(trained_file_path=self.data_inegestion_config.train_file_path,
                                                           test_file_path=self.data_inegestion_config.test_file_path)
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
        
            return data_ingestion_artifact
        except Exception as e:
            raise PorousException(e, sys) from e