# pi-envirophat

Experiments with the Raspberry Pi and [EnviroPhat](https://shop.pimoroni.com/products/enviro-phat)

## enviro-logger.py

Dumps the data from the EnviroPhat to a file - file writing isn't streamed

## enviro-json-output.py

Dumps the data from the EnviroPhat into a MongoDB collection (locally if installed or remote based on the `MONGO_DB` value in `.env`
