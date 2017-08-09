import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.test

# names = db.name

items = db.test.find_one()
print items