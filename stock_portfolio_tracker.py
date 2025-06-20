stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 130}

def main():
    print("Welcome to the Stock Portfolio Tracker!")
    try:
        num_stocks = int(input("How many different stocks do you want to enter? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Print available stock symbols
    print("\nAvailable stock symbols:")
    print(", ".join(stock_prices.keys()))

    portfolio = []
    total_investment = 0

    for i in range(num_stocks):
        symbol = input(f"Enter stock symbol #{i+1} (e.g., 'AAPL'): ").upper()
        if symbol not in stock_prices:
            print(f"Symbol '{symbol}' not found in price list. Skipping.")
            continue
        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
        except ValueError:
            print("Invalid quantity. Skipping this stock.")
            continue
        price = stock_prices[symbol]
        investment = price * quantity
        portfolio.append({
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'investment': investment
        })
        total_investment += investment

    print("\nPortfolio Summary:")
    for stock in portfolio:
        print(f"{stock['symbol']}: {stock['quantity']} shares x ${stock['price']} = ${stock['investment']}")
    print(f"\nTotal Investment Value: ${total_investment}")

    save = input("\nDo you want to save the results? (yes/no): ").strip().lower()
    if save in ("yes", "y"): 
        filetype = input("Save as .txt or .csv? (txt/csv): ").strip().lower()
        if filetype == "csv":
            filename = "portfolio.csv"
            with open(filename, "w") as f:
                f.write("Symbol,Quantity,Price,Investment\n")
                for stock in portfolio:
                    f.write(f"{stock['symbol']},{stock['quantity']},{stock['price']},{stock['investment']}\n")
            print(f"Results saved to {filename}")
        else:
            filename = "portfolio.txt"
            with open(filename, "w") as f:
                f.write("Portfolio Summary:\n")
                for stock in portfolio:
                    f.write(f"{stock['symbol']}: {stock['quantity']} shares x ${stock['price']} = ${stock['investment']}\n")
                f.write(f"\nTotal Investment Value: ${total_investment}\n")
            print(f"Results saved to {filename}")

if __name__ == "__main__":
    main() 