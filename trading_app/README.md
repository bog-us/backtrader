# Trading App

This directory contains a minimal trading application using **Backtrader** and
**Alpaca** together with placeholder integrations for LLM-based assistants.

## Structure

- `backend` - FastAPI backend exposing basic endpoints.
- `llm_integrations` - Abstraction layer for AI models.
- `strategies` - Trading strategies for Backtrader.
- `config` - Configuration management using Pydantic.
- `tests` - Pytest unit tests.

## Quickstart

1. Install dependencies:

```bash
pip install fastapi alpaca-trade-api pydantic backtrader uvicorn
```

2. Set environment variables (or create a `.env` file):

```bash
export TRADING_APP_ALPACA_KEY="<your-key>"
export TRADING_APP_ALPACA_SECRET="<your-secret>"
```

3. Run the API server:

```bash
uvicorn trading_app.backend.main:app --reload
```

4. Execute tests:

```bash
pytest trading_app/tests
```

This is a starting point for further development, including UI integrations,
database storage and richer LLM support.
