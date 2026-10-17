# Coin Market Track App

A desktop cryptocurrency portfolio tracker built with Python and Tkinter. The app connects to the CoinMarketCap API, stores your portfolio in SQLite, and shows your current holdings, total cost, current value, and profit/loss calculations in a simple GUI.

## Features

- Track multiple cryptocurrencies in one portfolio
- Add, update, and remove portfolio entries
- Fetch live market pricing from CoinMarketCap
- Display portfolio totals and per-coin profit/loss
- Persist holdings locally with SQLite
- Built as a desktop app using Tkinter

## Tech Stack

- Python 3
- Tkinter
- SQLite3
- Requests
- CoinMarketCap API

## Project Structure

```text
Coin-Market-Track-App/
├── portfolio.py
├── portfolio.spec
├── favicon.ico
├── coin.db
├── README.md
├── portfolio.exe
└── .gitignore (if present in your repo)
```

## Requirements

Before running the app, make sure you have:

- Python 3.8 or newer
- `pip` installed
- Internet access to reach the CoinMarketCap API

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

3. Run the application:

```bash
python portfolio.py
```

## How It Works

- The app creates a `coin.db` SQLite database automatically if it does not exist.
- Each portfolio entry includes the coin symbol, amount held, and purchase price.
- The app fetches the latest crypto listings from CoinMarketCap and matches them by symbol.
- It calculates:
  - total amount paid
  - current value
  - profit/loss per coin
  - total portfolio profit/loss

## Database Schema

The app uses a SQLite table named `crypto` with this structure:

```sql
CREATE TABLE IF NOT EXISTS crypto(
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    amount INTEGER,
    price REAL
)
```

## Notes

- The app currently stores the API key directly in the source file. In a production environment, it is better to store this in an environment variable or config file.
- The app is designed for personal portfolio tracking and educational use.
- The UI is not a modern web app; it is a simple Tkinter-based desktop interface.

## License

This project does not currently include a license file. If you plan to publish or share the project, consider adding an open-source license such as MIT.

## Disclaimer

This application is intended for personal tracking and educational purposes only. Always verify prices and financial information before making investment decisions.
