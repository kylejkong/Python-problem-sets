import json
import requests
import sys


def main():
    convert()


def convert():

    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    elif sys.argv[1]:

        try:

            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

            o = r.json()

            # print(json.dumps(r.json(), indent=2))

            amount = o["bpi"]["USD"]["rate_float"]

            n = float(sys.argv[1])

            amount = amount * n

            print(f"${amount:,.4f}")



        except requests.RequestException:

            sys.exit("Command-line is not an argument")





main()