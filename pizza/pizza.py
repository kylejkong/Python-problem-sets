import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")


elif sys.argv[1].endswith(".csv")==False:
    sys.exit("Not a CSV File")

elif len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as file:
            r = csv.DictReader(file)
            print(tabulate(r, tablefmt="grid", headers='keys'))


    except FileNotFoundError:
        sys.exit("File does not exist")





