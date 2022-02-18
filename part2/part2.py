import sys
import json

if __name__ == '__main__':

    # splitting the comma-separated values in the command line arguments
    stock = sys.argv[1]
    stock = stock.split(',')

    # converting list of strings to list of integers
    stock = [int(i) for i in stock]

    # initializing min_ value with the stock price of day 0 and max_profit value with 0
    min_ = stock[0]
    max_profit = 0

    # iterating through the list of stock prices for all days except day 0
    for i in stock[1:]:
        min_ = min(i, min_)
        max_profit = max(i - min_, max_profit)

    print(max_profit)
