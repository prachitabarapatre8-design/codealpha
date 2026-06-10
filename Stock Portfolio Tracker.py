# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150
}

total_investment = 0

stock_name = input("Enter stock name (AAPL/TSLA/GOOG): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total_investment = stocks[stock_name] * quantity
    print("Total Investment Value:", total_investment)

    # Save result to a text file
    file = open("portfolio.txt", "w")
    file.write("Stock: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Investment Value: " + str(total_investment))
    file.close()

    print("Result saved in portfolio.txt")
else:
    print("Stock not found!")