from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sharmalakshya341:sharmalakshya@cluster0.ftb81fm.mongodb.net/info?retryWrites=true&w=majority"


conn = MongoClient(uri)
