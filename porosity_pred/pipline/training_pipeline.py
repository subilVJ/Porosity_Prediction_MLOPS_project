import os
import sys
from porosity_pred.logger import logging
from porosity_pred.exception import PorousException
from porosity_pred.components.data_ingestion import DataIngestion
from porosity_pred.entity.config_entity import DataIngestionConfig
from porosity_pred.entity.artifact_entity import DataIngestionArtifact



class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.intiate_data_ingetsion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        except Exception as e:
            raise PorousException(e, sys) from e
        
    def run_pipline(self)->None:
        try:
            data_ingetion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise PorousException(e,sys)