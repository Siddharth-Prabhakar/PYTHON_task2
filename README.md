# Stock Portfolio Tracker

A simple Python script to track your stock investments and save your portfolio to a text or CSV file.

## Features
- Hardcoded stock prices for AAPL, TSLA, GOOGL, and AMZN
- User input for stock symbols and quantities
- Calculates and displays total investment
- Optionally saves results to `.txt` or `.csv` files
- Appends new results to existing files, preserving history

## Usage
1. Run the script:
   ```bash
   python stock_portfolio_tracker.py
   ```
2. Enter the number of different stocks you want to track.
3. Enter the stock symbol (choose from the displayed list).
4. Enter the quantity for each stock.
5. View your portfolio summary and total investment.
6. Choose whether to save the results and select the file format.

## Example Output
```
Welcome to the Stock Portfolio Tracker!
How many different stocks do you want to enter? 1

Available stock symbols:
AAPL, TSLA, GOOGL, AMZN
Enter stock symbol #1 (e.g., 'AAPL'): AAPL
Enter quantity for AAPL: 3

Portfolio Summary:
AAPL: 3 shares x $180 = $540

Total Investment Value: $540

Do you want to save the results? (yes/no): yes
Save as .txt or .csv? (txt/csv): txt
Results appended to portfolio.txt
```

## File Output Example (`portfolio.txt`)
```
Portfolio Summary:
AAPL: 3 shares x $180 = $540

Total Investment Value: $540
```

## License
See [LICENSE](LICENSE) for details.

---
**Created by SIDDHARTH PRBHAKAR** 