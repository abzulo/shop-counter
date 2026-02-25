# Shop Counter

A small command-line Python app for practicing modular design, file I/O, and testing.

## Features
- Shows available products with price and stock.
- Lets a user buy an item and quantity.
- Updates inventory in memory after each successful purchase.
- Saves each sale as a JSON line in `sales_history.json`.
- Displays previous sales history from file.

## Project Structure
- `shop_counter/data.py` — in-memory product catalog.
- `shop_counter/inventory.py` — product display + stock updates.
- `shop_counter/sales.py` — purchase flow + sale persistence.
- `shop_counter/main.py` — CLI menu entry point.
- `tests/` — pytest test suite.

## Run the Application
From the repository root:

```bash
python -m shop_counter.main
```

## Run Tests
From the repository root:

```bash
pytest -q
```

## Notes
- Sales are appended to a local `sales_history.json` file in your current working directory.
- Inventory resets each time you restart the app because product data is kept in memory.
