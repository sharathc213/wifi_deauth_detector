from pymongo import MongoClient
import json




f = open ('setup.json', "r")
data = json.loads(f.read())
f.close()
api=data['wifi']['deauther_detector']['sensor_pid']
adapter=data['wifi']['deauther_detector']['adapter_name_before']
database=data['wifi']['database']

client = MongoClient(database)

mock_data = {
    'deauthAttacks': [
        {
            'timestamp': '1574455535',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                'oui': '12:34:56',
                'company_name': 'Comcast',
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574455535',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574455535',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574455535',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574455535',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574469119',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574469119',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        },
        {
            'timestamp': '1574469119',
            'type': 'deauth',
            'victim': '00:14:22:01:23:45',
            'router': '00:99:99:00:99:00',
            'routerInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            },
            'victimInfo': {
                "oui": "12:34:56",
                'company_name': "Comcast",
                "company_address": "123 Main Street",
                "country_code": "US"
            }
        }
    ]
}

# Method to drop the deauth_attacks MongoDB database
def reset_db():
    print('Clearing database...')
    client.drop_database('deauth_attacks')


# Method to populate the deauth_attacks MongoDB database with mock data
def populate_db_with_mock_data():
    print('Populating database with mock data...')

    db = client['deauth_attacks']
    attacks = db['attacks']

    try:
        attacks.insert_many(mock_data['deauthAttacks'])
        print("sucess")
    except:
      print('ERROR: Failed to load mock data into the database. Message Cameron Cooper to fix it')
populate_db_with_mock_data()
