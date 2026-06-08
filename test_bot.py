import sqlite3
import pytest
import requests
from main import CryptoBot  # Assuming your bot is in CryptoBot.py

# The fake response we use to trick the API
class FakeResponse:
    def json(self):
        return {"USD": {"last": 60000}}

# Test 1: Verifies that the bot triggers a BUY when price is low
def test_crypto_bot_buy_status(monkeypatch):
    test_connection = sqlite3.connect(":memory:")
    bot = CryptoBot("BTC", 65000, test_connection)
    
    monkeypatch.setattr(requests, "get", lambda url: FakeResponse())
    
    message = bot.check_market()
    assert "Buy urgently!" in message

# Test 2: Verifies that the bot WAITS when price is high (Your Test!)
def test_crypto_bot_waiting_status(monkeypatch):
    test_connection = sqlite3.connect(":memory:")
    bot = CryptoBot("BTC", 50000, test_connection)
    
    monkeypatch.setattr(requests, "get", lambda url: FakeResponse())
    
    message = bot.check_market()
    assert "Still waiting..." in message

# Test 3: Verifies that data is properly written to the database (Your integration test!)
def test_crypto_bot_database_logging(monkeypatch):
    test_connection = sqlite3.connect(":memory:")
    bot = CryptoBot("BTC", 65000, test_connection)
    
    monkeypatch.setattr(requests, "get", lambda url: FakeResponse())
    bot.check_market()
    
    cursor = test_connection.cursor()
    cursor.execute("SELECT ticker, price, status FROM price_logs;")
    saved_data = cursor.fetchall()
    
    # Assert that the data was inserted correctly
    assert saved_data[0] == ("BTC", 60000.0, "BUY")