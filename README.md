# Coin Market Track App

A simple cryptocurrency portfolio tracker built with Python using the CoinMarketCap API to track coins' real-time values.

This project lets you keep track of your crypto holdings, view live market prices, and calculate profit/loss based on your entered purchase price and quantity.

This project contains a desktop app built with Tkinter and a local SQLite database for storing your portfolio data.

## Features

- Track multiple cryptocurrencies in one portfolio
- Add, update, and delete coin entries
- Fetch live crypto prices from CoinMarketCap
- Calculate amount paid, current value, and profit/loss
- Store portfolio data locally in SQLite
- Use a simple desktop GUI built with Tkinter

## Requirements

Make sure you have Python 3 installed.

Install the required package:

```bash
pip install requests
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/dircapwonder/Coin-Market-Track-App.git
cd Coin-Market-Track-App
```

2. Open `portfolio.py` and replace the placeholder API key:

```python
CMC_PRO_API_KEY=YOUR_API_KEY_HERE
```

with your actual CoinMarketCap API key.

3. Run the app:

```bash
python portfolio.py
```


## Project Structure

```text
Coin-Market-Track-App/
├── portfolio.py
├── favicon.ico
├── coin.db
├── portfolio.exe
├── portfolio.spec
├── README.md
└── .gitignore
```

## How It Works

The app creates a local SQLite database named `coin.db` if it does not exist.

Each portfolio entry stores:

- the coin symbol
- the amount owned
- the average purchase price

Then the app fetches the latest cryptocurrency listings from CoinMarketCap and matches them by symbol. It calculates:

- total amount paid
- current portfolio value
- profit/loss per coin
- total portfolio profit/loss

## Database Schema

The app uses a SQLite table named `crypto`:

```sql
CREATE TABLE IF NOT EXISTS crypto(
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    amount INTEGER,
    price REAL
)
```

## Example Workflow

1. Launch the app.
2. Add a coin using its symbol, price, and amount held.
3. Refresh the app to pull live prices.
4. Review the current value and profit/loss for each asset.


## Building an executable (.exe)

If you want to distribute the app as a standalone Windows executable, you can use PyInstaller. Install PyInstaller with:

```bash
pip install pyinstaller
```

From the repository root run the following:

```bash
python -m PyInstaller portfolio.py --onefile --noconsole --icon=favicon
```

## Why I Keep This Repo

This project is a simple personal portfolio tracker that helped me practice working with:

- Python
- Tkinter
- SQLite
- API requests
- Data processing and portfolio calculations

I wanted to keep this project in my GitHub because it was a useful way to bring together a few different skills in one small application.

## Disclaimer

This project is for personal tracking and learning purposes. Always verify pricing and financial calculations before making investment decisions.
