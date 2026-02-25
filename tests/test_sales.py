import json

from shop_counter.data import products
from shop_counter.sales import buy_item


def test_buy_item_saves_sale_record_and_updates_stock(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    buy_item("banana", 3)

    output = capsys.readouterr().out
    assert "You bought 3 banana(s) for 15 KES." in output
    assert products["banana"]["stock"] == 97

    lines = (tmp_path / "sales_history.json").read_text().splitlines()
    assert len(lines) == 1
    assert json.loads(lines[0]) == {"item": "banana", "quantity": 3, "total": 15}


def test_buy_item_does_not_write_history_on_invalid_purchase(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    buy_item("apple", 999)

    output = capsys.readouterr().out
    assert "Not enough stock or item not found." in output
    assert not (tmp_path / "sales_history.json").exists()
