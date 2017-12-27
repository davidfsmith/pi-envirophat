#!/usr/bin/python3

import time
from envirophat import light, motion, weather, leds

out = open('enviro.log', 'w')
out.write('light\trgb\tmotion\theading\ttemp\tpressure\n')

try:
    while True:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        out.write('%f\t%s\t%s\t%f\t%f\t%f\n' %
                  (lux, rgb, acc, heading, temp, press))
        time.sleep(10)

except KeyboardInterrupt:
    leds.off()
    out.close()
