from pymongo import MongoClient

mongoURI = "mongodb://db:27017"
conn = MongoClient()
print(conn)

db = conn["TODO"]
collection = db['todo']

def create(data):
    data = dict(data)
    response = collection.insert-one(data)
    return response.inserted_id

def all():
    response = collection.find({})
    return list(respose)

def get_one(condition):
    response = collection.find_one({'name':condition})
    return response

def update(name, data):
    response = collection.update_one({'name':name},{'$set':data})

def delete(name):
    response = collection.delete_one({'name':name})
    return response.deleted_count
