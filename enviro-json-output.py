#!/usr/bin/python3

import os
from os.path import join, dirname
from dotenv import load_dotenv

import argparse
import json
from datetime import datetime
from envirophat import light, motion, weather, leds
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DEBUG = os.getenv('DEBUG', None)
MONGO_DB_URL = os.getenv('MONGO_DB')

parser = argparse.ArgumentParser()
parser.add_argument('--location',
                    default='Unkown',
                    help='Location to descibe where the Pi is')
args = parser.parse_args()

leds.on()
rgb = str(light.rgb())[1:-1].replace(' ', '')
leds.off()
acc = str(motion.accelerometer())[1:-1].replace(' ', '')

data = {
    'location': args.location,
    'time': datetime.utcnow().isoformat(),
    'light': light.light(),
    'rgb': rgb,
    'motion': acc,
    'heading': motion.heading(),
    'temp': weather.temperature(),
    'pressure': weather.pressure(),
}

# json_data = json.dumps(data)
# print(json_data)

client = MongoClient(MONGO_DB_URL)

try:
    result = client.admin.command("ismaster")
    print("Connected to Mongo")
except ConnectionFailure as e:
    print(e)

db = client.test
enviro = db.enviro
id = enviro.insert_one(data).inserted_id

print(id)

client.close()
