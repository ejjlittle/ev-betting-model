from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

def setup():
    load_dotenv(dotenv_path='.env')
    uri = os.getenv("MONGO_URI")
    if not uri:
        raise ValueError("MONGO_URI is not set or is invalid in the .env file")

    client = MongoClient(uri)
    db = client["betting-data"]

    if "placed-bets" not in db.list_collection_names():
        raise ValueError("Collection 'placed-bets' does not exist in 'betting-data'")

    return db["placed-bets"]