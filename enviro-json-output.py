#!/usr/bin/python3

import argparse
import json
from datetime import datetime
from envirophat import light, motion, weather, leds

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

print(json.dumps(data))
