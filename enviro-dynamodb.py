#!/usr/bin/python3

import os
from os.path import join, dirname
from dotenv import load_dotenv

import boto3
import argparse
from datetime import datetime
from envirophat import light, motion, weather, leds

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DEBUG = os.getenv('DEBUG', None)

parser = argparse.ArgumentParser()
parser.add_argument('--account',
                    default='',
                    help='Account number for the device')
parser.add_argument('--location',
                    default='Unkown',
                    help='Location to descibe where the Pi is')
args = parser.parse_args()

leds.on()
rgb = str(light.rgb())[1:-1].replace(' ', '')
leds.off()
acc = str(motion.accelerometer())[1:-1].replace(' ', '')

device_uuid = 'f9d84855-aa86-4f9d-b773-effc1029f700'

session = boto3.Session(profile_name='PROFILE',
                        region_name='eu-west-1')
client = session.client('dynamodb')

r = client.put_item(
    TableName='Careline',
    Item={
        'device_uuid': {'S': device_uuid},
        'timestamp': {'S': datetime.now().isoformat()},
        'account': {'S': args.account},
        'location': {'S': args.location},
        'data': {'M': {
            'light': {'S': str(light.light())},
            'rgb': {'S': rgb},
            'motion': {'S': acc},
            'heading': {'S': str(motion.heading())},
            'temp': {'S': str(weather.temperature())},
            'pressure': {'S': str(weather.pressure())}, }
        }
    }
)
print(r)
