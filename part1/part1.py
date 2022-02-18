import sys
import json

if __name__ == '__main__':

    # opening 'stocks.json' file
    f = open('stocks.json')
    data = json.load(f)
    stock_info = {}

    # Copying contents from 'stocks.json' file to dictionary object 'stock_info' with ticker as key and close as value
    for i in data:
        stock_info[i['ticker']] = i['close']

    # splitting the comma-separated values in the command line arguments
    stock = sys.argv[1]
    stock = stock.split(',')

    # total stocks value
    total = 0.0

    # iterating through the arguments' list of stocks
    for s in stock:
        temp = s.split(':')
        ticker = temp[0]
        quantity = float(temp[1])
        total = total + (quantity * stock_info[ticker])

    print(total)


