__author__ = 'grobvincent'

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Medias

links = db.articles

cursor = links.find({},{"body":1})



test=""


for document in cursor :
    test = test+str(document)


print(test)