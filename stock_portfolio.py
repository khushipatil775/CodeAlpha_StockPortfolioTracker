
# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 300
}

total_investment = 0

print("Welcome to Stock Portfolio Tracker!")

while True:
    name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Enter a valid quantity!")
            continue

        investment = stocks[name] * quantity
        total_investment += investment

        print("Stock Price:", stocks[name])
        print("Investment:", investment)

    else:
        print("Stock not found!")

print("\nTotal Investment:", total_investment)
print("Thank you!")
