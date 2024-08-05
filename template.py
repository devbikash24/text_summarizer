import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummarizer"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", # __init__.py as python package
    f"src/{project_name}/componenet/__init__.py",
    f"src/{project_name}/utils/__init__.py", # contains utility functions and helper methods
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py", # contains logging functions
    f"src/{project_name}/config/__init__.py", #configuration functions
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # data processing pipelines
    f"src/{project_name}/entity/__init__.py", # contains constant values
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml",
    "params.yaml",
    "app.py", #main application entry point
    "main.py",
    "Dockerfile",
    "requirements.text",
    "setup.py", #script to package the project 
    "research/trails.ipynb",
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)    
        logging.info(f"Created directory: {filedir} for file name {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} is already exists")
