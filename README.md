# Coin Market Track App

A simple desktop cryptocurrency portfolio tracker built with Python. It pulls live prices from the [CoinMarketCap API](https://coinmarketcap.com/api/) and calculates your profit/loss based on the purchase price and quantity you enter.

The app uses a Tkinter GUI and stores your portfolio in a local SQLite database. It does **not** connect to any exchange or wallet, and it never trades or touches real funds.

## Features

- Track multiple cryptocurrencies in a single portfolio
- Add, update, and delete coin entries from the GUI
- Fetch live prices from CoinMarketCap
- See amount paid, current value, profit/loss per coin, and total portfolio profit/loss
- Profit and loss are color-coded (green for gain, red for loss)
- Local storage with SQLite, so no account or server is needed
- Optional standalone Windows `.exe` build with PyInstaller

## Requirements

- Python 3.8+
- A free [CoinMarketCap API key](https://coinmarketcap.com/api/)
- The `requests` library (Tkinter and SQLite ship with Python)

```bash
pip install requests
```

> **Platform note:** The window icon is set with an `.ico` file, which works on Windows. On Linux or macOS you may need to remove or change the `iconbitmap("favicon.ico")` line in `portfolio.py`.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/dircapwonder/Coin-Market-Track-App.git
   cd Coin-Market-Track-App
   ```

2. Open `portfolio.py` and replace the placeholder in the API URL with your own key:

   ```
   CMC_PRO_API_KEY=YOUR_API_KEY_HERE
   ```

3. Run the app:

   ```bash
   python portfolio.py
   ```

> **Security note:** Do not commit your real API key to GitHub. Consider reading it from an environment variable instead of hardcoding it.

## Usage

| Action | How |
|---|---|
| **Add a coin** | Enter the coin symbol (e.g. `BTC`), your purchase price, and the amount in the bottom row of the table, then click **Add Coin**. |
| **Update a coin** | Enter the Portfolio ID of the entry plus the new symbol, price, and amount, then click **Update Coin**. |
| **Delete a coin** | Enter the Portfolio ID and click **Delete Coin**. |
| **Refresh prices** | Click **Refresh** to fetch the latest prices and recalculate everything. |
| **Clear everything** | Use **File → Clear All** to delete all entries. |

The table shows these columns for each coin: Portfolio ID, Coin Name, Price, Amount Owned, Amount Paid, Current Value, P/L per Coin, and P/L Total Coin. The last row shows the totals and the overall wallet profit/loss.

## How It Works

On startup the app creates a local SQLite database named `coin.db` if it doesn't already exist. Each portfolio entry stores:

- the coin symbol
- the amount owned
- the purchase price

The app then requests the latest listings from CoinMarketCap, matches your coins by symbol, and calculates:

- **Amount paid** = amount × purchase price
- **Current value** = amount × current price
- **P/L per coin** = current price − purchase price
- **Total P/L** = P/L per coin × amount, summed across the portfolio

### Database schema

```sql
CREATE TABLE IF NOT EXISTS crypto(
    id INTEGER PRIMARY KEY,
    symbol TEXT,
    amount INTEGER,
    price REAL
)
```

### About the included `coin.db`

The `coin.db` file in this repository is just sample data used for demonstration. You can delete it, and the app will create a fresh, empty one on the next launch.

## Project Structure

```text
Coin-Market-Track-App/
├── portfolio.py     # Main application (GUI, database, API calls)
├── favicon.ico      # Window and executable icon
├── coin.db          # Local SQLite database (sample data)
├── portfolio.spec   # PyInstaller build configuration
├── portfolio.exe    # Prebuilt Windows executable
└── README.md
```

## Building a Windows Executable

You can package the app as a standalone `.exe` with PyInstaller:

```bash
pip install pyinstaller
python -m PyInstaller portfolio.py --onefile --noconsole --icon=favicon.ico
```

- `--onefile` bundles everything into a single executable.
- `--noconsole` hides the console window (omit it if you want to see output while debugging).
- `--icon=favicon.ico` sets the executable's icon.
- The finished file appears in the `dist/` folder.

**Important:** The app loads `favicon.ico` and `coin.db` using relative paths, and `favicon.ico` is not bundled into the executable. Keep `portfolio.exe` in the same folder as `favicon.ico` (and `coin.db`, if you want to keep an existing portfolio), and run it from that folder. Antivirus software can occasionally flag PyInstaller executables, so test the build on the target machine.

## Limitations

- Only the top 250 coins by market cap are fetched, so coins ranked lower are not matched.
- Coins are matched by symbol only, and each refresh makes one API request, so keep CoinMarketCap's free-tier request limits in mind.
- The app does not handle network or API errors gracefully yet.
- Input fields are not validated, so enter numbers carefully.

## Ideas for Improvement

- Move the API key to an environment variable or config file
- Add error handling and input validation
- Support fractional amounts with a `REAL` column instead of `INTEGER`
- Refresh prices automatically on a timer
- Show portfolio history or charts

## Why This Project

This is a small personal project that let me practice Python, Tkinter, SQLite, REST API requests, and basic portfolio calculations in one application.

## Disclaimer

This project is for personal tracking and learning purposes only and is not financial advice. Always verify prices and calculations before making investment decisions.
