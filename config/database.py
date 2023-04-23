from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
username = os.environ.get('user')
password = os.environ.get('pass')
uri = f'mongodb+srv://{username}:{password}@cluster0.ftb81fm.mongodb.net/info?retryWrites=true&w=majorityf'


conn = MongoClient(uri)
