#!/usr/bin/python3

import json
from datetime import datetime
from envirophat import light, motion, weather, leds


leds.on()
rgb = str(light.rgb())[1:-1].replace(' ', '')
leds.off()
acc = str(motion.accelerometer())[1:-1].replace(' ', '')

data = {
    'light': light.light(),
    'rgb': rgb,
    'motion': acc,
    'heading': motion.heading(),
    'temp': weather.temperature(),
    'pressure': weather.pressure(),
}

print(json.dumps(data))
