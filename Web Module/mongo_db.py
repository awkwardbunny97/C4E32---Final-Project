import pymongo


client = pymongo.MongoClient("mongodb+srv://c4e32:c4e32@cluster0-ayiyv.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.products

