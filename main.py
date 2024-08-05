
import os
import sys

# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from textsummarizer.logging import logger


logger.info("welcome to the logs")