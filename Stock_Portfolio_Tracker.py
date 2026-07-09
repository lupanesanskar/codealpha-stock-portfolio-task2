# Stock Portfolio Tracker

# dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

total_investment = 0
portfolio = []

print("Welcome to Stock Portfolio Tracker")
print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        portfolio.append(
            stock_name + " - Quantity: " + str(quantity)
            + " - Value: $" + str(investment)
        )

        print("Investment Value: $", investment)

    else:
        print("Stock not available.")

print("\n--- Portfolio Summary ---")

for stock in portfolio:
    print(stock)

print("\nTotal Investment Value: $", total_investment)

# file handling
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")

    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock in portfolio:
        file.write(stock + "\n")

    file.write("\nTotal Investment Value: $" + str(total_investment))

    file.close()

    print("Portfolio saved successfully in portfolio.txt")