# We have in the code below: OOP, Automation, API, Web, and Database. 
import sqlite3
import requests
import time

class CryptoBot: 
    def __init__(self, name, target_price, connection):
        self.name = name
        self.target_price = target_price
        self.connection = connection
        self.cursor = self.connection.cursor()
        
        # Create table using SQL syntax
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS price_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT,
                price REAL,
                status TEXT
            );
        """)
    
    def check_market(self):
        url = "https://blockchain.info/ticker"
        
        response = requests.get(url)
        data = response.json()
        price = data["USD"]["last"]

        if price <= self.target_price:
            status = 'BUY'
            message = f"🚨🚨🚨 {self.name} Reached target price! Buy urgently! 🚨🚨🚨"
        else:
            status = 'WAITING'
            message = f"⏳ Still waiting..."
        
        # Dynamically insert the data
        self.cursor.execute("INSERT INTO price_logs (ticker, price, status) VALUES (?, ?, ?);", (self.name, price, status))
        self.connection.commit()

        # Fetch and verify database logs
        self.cursor.execute("SELECT * FROM price_logs;")
        all_stocks = self.cursor.fetchall()
        print("Database Content:", all_stocks)
        
        return message

# 1. Create the database connection ONCE outside the class
shared_connection = sqlite3.connect("crypto_tracker.db")
btc = CryptoBot("BTC", 64200, shared_connection)

if __name__ == "__main__":
    while True:
        print(btc.check_market())
        time.sleep(5)

# (Optional) Close connection when the whole program completely stops
# shared_connection.close()
