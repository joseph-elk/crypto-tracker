# Crypto Tracker Bot

An automated Python-based cryptocurrency tracking application that monitors real-time market prices and logs market status into a local database.

## Description
This bot connects to a live blockchain API to fetch the latest price of Bitcoin (BTC) every 5 seconds. Based on a user-defined target price, the bot dynamically determines whether it is time to execute a "BUY" order or remain "WAITING". All tracked data and execution statuses are securely logged and stored in an SQLite database using an optimized object-oriented architecture.

## Tech Stack
* **Language:** Python 3
* **Libraries:** Requests (API communication), Time (automation control)
* **Database:** SQLite3 (Structured SQL data logging)
* **Version Control:** Git & GitHub

## Architecture & Best Practices
* **Dependency Injection:** Database connection is injected through the class constructor to optimize resource consumption.
* **DRY Principle:** Refactored code structure to prevent repetitive database operations.
* **Security:** Configured `.gitignore` to prevent local runtime database logs (`.db`) from being exposed in the public repository.

## Running Tests
This project includes an automated test suite developed with `pytest` to verify the bot's logic and database integration.

To install dependencies and run the tests, execute the following commands in your terminal:
```bash
pip install pytest requests
pytest