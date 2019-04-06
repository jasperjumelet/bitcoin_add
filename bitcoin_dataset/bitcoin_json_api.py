import json
from urllib.request import urlopen
import time
import sys

def databaseupdater(n):
	while True:
		for i in range(n):
			time.sleep(1)
		with urlopen("https://api.coindesk.com/v1/bpi/currentprice.json") as response:
			source = response.read()

		data = json.loads(source)

		# You can also open your own dataset in a json format.
		with open("example_data.json", "a") as bitcoindataset:
			bitcoindataset.write(str(data))

def main():
	try:
		if sys.argv[1] == "d".lower():
			databaseupdater(86400)
		elif sys.argv[1] == "h".lower():
			databaseupdater(3600)
		elif sys.argv[1] == "m".lower():
			databaseupdater(60)
		else:	
			databaseupdater(int(sys.argv[1]))
	except:
		print("Pls choose d for a day, h for an hour, m for a minute in standard input. \nOr you can put an integer to say how many seconds it does to refresh")

if __name__ == "__main__":
	main()
	


