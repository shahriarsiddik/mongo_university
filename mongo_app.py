import bottle
import pymongo

@bottle.route('/')
def index():
    connection = pymongo.MongoClient('localhost',27017)
    db = connection.test

    item = db.test.find_one()

    return '<b>Hello %s' % item['name']

bottle.run(host='localhost', port=8082)