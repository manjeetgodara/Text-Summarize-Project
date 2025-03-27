import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from box import  ConfigBox
from pathlib import Path
from typing import Any
from ensure import ensure_annotations

#Function to read any yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            contents = yaml.safe_load(yaml_file)
            logger.info(f"Loaded {path_to_yaml} successfully")
            return ConfigBox(contents)
            # return contents if contents else {}
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

#Function to create directories
@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    for path_to_directory in path_to_directories:
        os.makedirs(path_to_directory, exist_ok=True)
        if verbose:
            logger.info(f"Created directory {path_to_directory} successfully")


#To get the size of the file
@ensure_annotations
def get_size(path:Path)-> str:
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"~ {size_in_kb} KB"




