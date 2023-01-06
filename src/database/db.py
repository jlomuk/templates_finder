import motor.motor_asyncio

from settings import MONGODB_URL, MONGO_DATABASE
from settings import logger

mongo_connection = None


def connect_db():
    """init connect to mongo and database"""
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
    db = client[MONGO_DATABASE]
    logger.info('Connected to MongoDb -- connection settings: %s', db)
    global mongo_connection
    mongo_connection = db


def get_db() -> motor.motor_asyncio.AsyncIOMotorDatabase:
    """get connection for mongo"""
    return mongo_connection


async def find_all_forms(db) -> dict[str, dict]:
    """fetch all struct forms"""
    templates: dict[str, dict] = {}
    async for document in db.templates.find():
        template = {key: value for key, value in document.items() if key not in ("_id", "name")}
        templates[document['name']] = template
    return templates

