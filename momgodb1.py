import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.gnfzi6p.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {"name":"gaurav", "surname":"singh", "email":"gs@gmail.com"}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)