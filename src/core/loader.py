import logging.config
import os

import nltk

from core.config import settings

# init logger
logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger("default")

# init nltk
nltk.data.path = [os.path.abspath(settings.NLTK_DATA_PATH)]


def init_nltk():
    for dataset, path in zip(settings.NLTK_DATASETS, settings.NLTK_DATASETS_LOCATIONS):
        try:
            nltk.data.find(path)
        except LookupError:
            nltk.download(dataset, download_dir=settings.NLTK_DATA_PATH)
