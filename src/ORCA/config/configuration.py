from ORCA.constants import *
from ORCA.utils.common import read_yaml, create_directories
from ORCA.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)
        create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config['data_ingestion']
        create_directories([config['root_dir']])

        return DataIngestionConfig(
            root_dir=Path(config['root_dir']),
            local_data_file=Path(config['local_data_file'])
        )