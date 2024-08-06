import os
from box.exceptions import BoxValueError
import yaml 
from textsummarizer.logging import logger
from ensure import ensure_annotations # used to enforce type annotations at runtime.
from box import ConfigBox # provide way to work with nested dictionaries using dot notation.
from pathlib import Path
from typing import Any #any from  the typing module is used for type hints to indicate that a variable can be of any type.


@ensure_annotations 
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    Read a yaml file and convert it into a ConfigBox object.

    Args: 
        Path to the yaml file
    Raises: 
        ValueError: if yaml file is empty
    Returns:
        ConfigBox: ConfigBox type

    """
    if not path_to_yaml.exists():
        logger.error(f"Config file does not exist at path: {path_to_yaml}")
        raise FileNotFoundError(f"Config file does not exist at path: {path_to_yaml}")
    
    try:
        with open(path_to_yaml, 'r') as file:
            data = yaml.safe_load(file)
            if data is None:
                logger.error("YAML file is empty")
                raise ValueError("YAML file is empty")
            logger.info("yaml_file: {path_to_yaml} load successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except yaml.YAMLError as e:
        logger.error(f"Error reading YAML file: {e}")
        raise ValueError("Error reading YAML file") from e
    except BoxValueError as e:
        logger.error(f"Error converting YAML data to ConfigBox: {e}")
        raise ValueError("Error converting YAML data to ConfigBox") from e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """

    for directory_path in path_to_directories:
        directory_path = Path(directory_path)
        try:
            os.makedirs(directory_path, exist_ok=True)
            if verbose:
                if directory_path.exists():
                        logger.info(f"Directory already exists: {directory_path}")
                else:
                    logger.info(f"Created directory: {directory_path}")
        except Exception as e:
            logger.error(f"Failed to create directory {directory_path}: {e}")

@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"