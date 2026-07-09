# Stock Portfolio Tracker 📈

This is **Task 2** of my **CodeAlpha Python Programming Internship**.

## About the Project
A command-line **Stock Portfolio Tracker** built in Python. It lets the user add stocks from a predefined list, calculates the total investment value, displays a portfolio summary, and optionally saves the results to a text file.

## Features
- Predefined dictionary of stock prices (AAPL, TSLA, GOOGL, MSFT, AMZN)
- User can enter stock names and quantities to build a portfolio
- Automatically calculates investment value per stock and total portfolio value
- Validates stock names against the available list
- Displays a full portfolio summary at the end
- Option to save the summary to a `portfolio.txt` file (file handling)

## Tech Stack
- **Language:** Python 3
- **Concepts used:** Dictionaries, lists, loops, conditionals, file handling (I/O)

## How to Run
1. Clone this repository
   ```bash
   git clone https://github.com/lupanesanskar/codealpha-stock-portfolio-task2
   cd codealpha-stock-portfolio-task2
   ```
2. Run the script
   ```bash
   python stock_portfolio_tracker.py
   ```
3. Enter stock names (e.g. `AAPL`, `TSLA`) and quantities when prompted. Type `done` when finished to see your portfolio summary.

## Sample Run
```
Welcome to Stock Portfolio Tracker
Available Stocks: ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'AMZN']

Enter stock name (or 'done' to finish): AAPL
Enter quantity: 10
Investment Value: $ 1800

Enter stock name (or 'done' to finish): done

--- Portfolio Summary ---
AAPL - Quantity: 10 - Value: $1800

Total Investment Value: $ 1800

Do you want to save the result? (yes/no): yes
Portfolio saved successfully in portfolio.txt
```

## Project Structure
```
─ stock_portfolio_tracker.py   # Main program logic
─ README.md                    # Project documentation
```

## Future Improvements
- Fetch real-time stock prices using a live API (e.g. Alpha Vantage, Yahoo Finance)
- Add support for removing/editing stocks from the portfolio
- Show percentage allocation per stock in a chart
- Build a GUI or web version using Tkinter/Streamlit

## Acknowledgment
This project was completed as part of the **CodeAlpha Internship Program** – Python Programming Track (Task 2).

---
