# Execution Instructions - Future Capital Coding Interview

Clone GitHub repo and goto repo directory


##  Part  1  -  Calculate  the  total  value  of  a  stock  portfolio

A sample stock portfolio is passed in as an argument to a console application. Your application should parse this input, lookup the current stock price at close from the sample [stocks.json](https://raw.githubusercontent.com/pronvest/interview/master/backend/stocks.json) feed file, and then return the total value of the portfolio.

Run test cases with the following commands. Additional test cases can be passed as an argument of string with comma-separated values like below.

###  Test Cases

1) `python part1.py "FB:12,PLTR:5000" `

2) `python part1.py "BABA:1,TSLA:5,WISH:1200" `
### Output
The output is displayed in the terminal window in which the above commands are run.

1) `119887.4`
2) `9891.9`

## Part 2 - Maximize profits

An analyst has developed an equation for predicting future stock prices. A client wants to use this algorithm to place a buy order at the optimum time and one sell order at the optimum time. You are provided a list of `prices` where `prices[i]` is the price of a given stock on the `ith` day. You want to maximize your profit by choosing a single day to buy one stock and choosing one different day to sell in the future. Due to trade restrictions, you may only place one buy order and one sell order. Return the maximum profit that the client can achieve from this transaction. If the client cannot achieve any profit, then return 0. Your application should work for any random list of prices.


### Input

1) `python part2.py "7,1,5,3,6,4"` 

2) ` python part2.py "7,6,4,3,1"`


### Output
The output is displayed in the terminal window in which the above commands are run.
1) `5`
2) `0`
