import os
from typing import Any, Dict, List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    # base settings
    APP_NAME: str = "NLTK Project"
    DEBUG: int = os.getenv("DEBUG", 1)
    PORT: int = os.getenv("PORT", 8000)

    # nltk settings
    NLTK_DATA_PATH: str = os.getenv("NLTK_DATA_PATH", "./../nltk_data/")

    NLTK_DATASETS: List[str] = [
        'punkt',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words',
    ]

    # nltk datasets path locations to verify that they are installed
    NLTK_DATASETS_LOCATIONS: List[str] = [
        'tokenizers/punkt',
        'taggers/averaged_perceptron_tagger',
        'chunkers/maxent_ne_chunker',
        'corpora/words'
    ]

    # logger config
    # modify for better experience
    LOGGING_CONFIG: Dict[str, Any] = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'formatters': {
            'verbose': {
                'format': '%(asctime)s.%(msecs)03d | %(levelname)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'loggers': {
            'default': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        },
    }


settings = Settings()
