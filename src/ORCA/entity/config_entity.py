import os
from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    data_file_path: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    transformed_data_path: Path
    data_input_path: str
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    learning_rate: float
    n_estimators: float
    target_column: float

