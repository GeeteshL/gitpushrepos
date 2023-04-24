import pymongo
client = pymongo.MongoClient("mongodb+srv://geetesh30:<30Geetesh>@cluster0.vu1boyg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "geetesh",
    "email" : "geetesh@gmail.com",
    "surname"  : "kbbnsa"
    }
db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d )