from pymongo import MongoClient

mongoURI = "mongodb://db:27017"
conn = MongoClient()
print(conn)
