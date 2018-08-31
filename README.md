# pi-envirophat

Experiments with the Raspberry Pi and [EnviroPhat](https://shop.pimoroni.com/products/enviro-phat)

## enviro-logger.py

Dumps the data from the EnviroPhat to a file - file writing isn't streamed

## enviro-json-output.py

Dumps the data from the EnviroPhat into a MongoDB collection (locally if installed or remote based on the `MONGO_DB` value in `.env`

## enviro-dynamodb.py

Dumps the data from the EnvironPhat into a DyanmoDB table (needs to be created first) AWS authentication is handled using the AWS CLI so you should have the following in `~/.aws/credentials`

	[profile-name]
	aws_access_key_id = access_key_id
	aws_secret_access_key = aws_secret_access_key
	
The `profile-name` needs to be set in `.env` file as well as the `region` and `table` name.

Running the code requires the following values:

* `--account` made up account number / string
* `--location` location of the recording device

Tested and working on a [Pi Zero WH](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header) and [Pi 3 B+](https://shop.pimoroni.com/products/raspberry-pi-3-b-plus)

### Todo

1. Use env to set profile name / region and table name
2. 	If response != 200 when logging the data to DyanmoDB do something with it (log file?)
