import logging
import os
from logging.config import dictConfig

from logger import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("Templates")

# MongoDB settings
MONGO_USER = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
MONGO_PASS = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
MONGO_DATABASE = os.environ.get('MONGO_INITDB_DATABASE')
MONGODB_URL = f"mongodb://{MONGO_USER}:{MONGO_PASS}@mongo:27017/"
