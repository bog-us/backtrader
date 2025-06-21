"""FastAPI backend for trading application."""
from fastapi import FastAPI
from alpaca_trade_api.rest import REST

from trading_app.config.config import settings

app = FastAPI(title="Trading App")


@app.get("/account")
def read_account():
    """Return Alpaca account information."""
    api = REST(settings.alpaca_key, settings.alpaca_secret, settings.alpaca_endpoint)
    account = api.get_account()._raw
    return account
