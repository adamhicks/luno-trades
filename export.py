import argparse
import csv
from time import sleep

from luno_python.client import Client

def fetch_trades(pair, api_key, api_secret):
	c = Client(api_key_id=api_key, api_key_secret=api_secret)

	upto = 0
	all_trades = []

	while True:
		res = c.list_user_trades(pair, after_seq=upto+1, limit=100)
		trades = res["trades"]
		if not trades:
			break
		all_trades.extend(trades)

		print("got " + str(len(all_trades)) + " trades so far...")
		sleep(1)
		upto = trades[-1]["sequence"]

	print("got " + str(len(all_trades)) + " total trades.")
	return all_trades


def write_trades_csv(trades, csv_name):
	fields = [
		"pair","sequence","order_id","type","timestamp",
		"price","volume","base","counter","fee_base","fee_counter",
	]

	with open(csv_name, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fields, extrasaction="ignore")
		writer.writeheader()
		for t in trades:
			writer.writerow(t)

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--pair', required=True, help='the market we will be exporting trades for e.g. XBTEUR')
	parser.add_argument('--key', required=True, help='the key part of the api key')
	parser.add_argument('--secret', required=True, help='the secret part of the api key')
	parser.add_argument('--output', default="trades.csv", help='the .csv file to write to, defaults to  "trades.csv"')

	args = parser.parse_args()

	trades = fetch_trades(args.pair, args.key, args.secret)
	write_trades_csv(trades, args.output)

if __name__ == "__main__":
	main()