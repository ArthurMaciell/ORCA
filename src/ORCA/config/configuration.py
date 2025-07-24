from ORCA.constants import *
from ORCA.utils.common import read_yaml, create_directories
from ORCA.entity.config_entity import DataIngestionConfig
from ORCA.entity.config_entity import DataValidationConfig


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
        


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.columns

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            data_file_path = config.data_file_path,
            all_schema=schema,
        )

        return data_validation_config