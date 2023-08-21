import sys
from flask import Flask, jsonify
from bson.json_util import dumps
from flask_cors import CORS
from pymongo import MongoClient
from db_utils import reset_db, populate_db_with_mock_data
import json

f = open ('setup.json', "r")
data = json.loads(f.read())
f.close()
api=data['wifi']['deauther_detector']['sensor_pid']
adapter=data['wifi']['deauther_detector']['adapter_name_before']
database=data['wifi']['database']


app = Flask(__name__)

# Allow all origins
CORS(app, resources={r'*': {'origins': '*'}})

# MongoDB Setup
client = MongoClient(database)
db = client['deauth_attacks']
attacksCollection = db['attacks']
lastAttackCollection = db['lastAttack']


@app.route('/')
def index():
   
        
       
    response = {
                "lastAttack": "",
                "deauthAttacks": attacksCollection.find()
            }
    return dumps(response)
            



if __name__ == '__main__':
    if sys.argv[1] == 'mock_data':
        reset_db()
        populate_db_with_mock_data()

    if sys.argv[1] == 'reset_db':
        reset_db()

    app.run()
