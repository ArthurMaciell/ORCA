from ORCA.utils.common import get_size
from ORCA import logger
import os
import urllib.request as request
import zipfile
from pathlib import Path
from ORCA.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def verify_local_file(self):
        path = self.config.local_data_file
        if os.path.exists(path):
            logger.info(f"Arquivo encontrado: {path} ({get_size(Path(path))})")
        else:
            raise FileNotFoundError(f"O arquivo {path} não foi encontrado. Coloque o Excel nessa pasta.")