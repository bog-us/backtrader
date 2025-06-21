from trading_app.config.config import Settings


def test_settings_load(monkeypatch):
    monkeypatch.setenv("TRADING_APP_ALPACA_KEY", "key")
    monkeypatch.setenv("TRADING_APP_ALPACA_SECRET", "secret")
    s = Settings()
    assert s.alpaca_key == "key"
    assert s.alpaca_secret == "secret"
