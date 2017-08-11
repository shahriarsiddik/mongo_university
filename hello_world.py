import bottle
import pymongo

@bottle.route('/')
def hello_world():
    connection = pymongo.MongoClient('localhost',27017)
    db = connection.test
    allNames = db.test.find()
    return bottle.template('hello_world',names = allNames)

@bottle.post('/fav_person')
def fav_person():
    person = bottle.request.forms.get("person")
    if person == None or person == "":
        person = "No person selected"
    print person
    bottle.response.set_cookie("person",person)
    return bottle.redirect('/fav_movies')

@bottle.route('/fav_movies')
def fav_movies():
    person = bottle.request.get_cookie("person")
    return bottle.template('fav_person',{'person':person})

bottle.debug(True)
bottle.run(host='localhost',port=8080)

