
import pymongo

client = pymongo.MongoClient('mongodb://52.79.169.68/:27017/')
db = client.KBO
collection = db.game
