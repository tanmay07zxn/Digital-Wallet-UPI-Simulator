# Digital Wallet and UPI Transaction Simulator

A beginner-level Python command-line project that simulates basic digital wallet and UPI operations.

## Overview

The project allows a user to create a wallet, log in, add simulated money, transfer money to another registered UPI ID, check the balance, and view transaction history.

**Important:** This is only an educational simulation. It does not perform real UPI or bank transactions.

## Features

- Wallet registration
- UPI ID validation
- 4-digit PIN validation
- Login
- Balance checking
- Add money
- UPI-style money transfer
- Transaction history
- CSV-based local storage
- Basic error handling
- Simple unit tests

## Technologies Used

- Python 3
- Functions and basic classes
- `csv` module
- `os` module
- `unittest` module for testing

No JSON database is used.

## Project Structure

```text
digital_wallet_upi_simulator/
│
├── main.py
├── wallet.py
├── user.py
├── transaction.py
├── storage.py
├── validation.py
├── statement.md
├── README.md
│
├── data/
│   ├── users.csv
│   └── transactions.csv
│
└── tests/
    └── test_wallet.py
```

## How to Run

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

4. Select **Create Wallet**.
5. Create another wallet in a second run if you want to test a transfer.
6. Login and use the wallet menu.

## How to Test

Run:

```bash
python -m unittest discover -s tests
```

The tests check adding money, sending money, failed transfers and a successful wallet-to-wallet transaction.

## Data Storage

The project uses two CSV files:

- `data/users.csv` stores name, UPI ID, PIN and balance.
- `data/transactions.csv` stores transfer details and status.

These files are intentionally simple so that a beginner can open and understand them.

## Limitations

- It is not connected to real UPI.
- There is no real bank account.
- PINs are stored as plain text because this is a basic educational simulator.
- It is designed for local learning, not production use.

## Future Enhancements

- Better password/PIN protection
- Transaction IDs
- Date and time for transactions
- Recharge and bill-payment simulation
- Admin dashboard
- A graphical user interface
