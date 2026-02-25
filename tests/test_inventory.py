from shop_counter.data import products
from shop_counter.inventory import update_stock


def test_update_stock_reduces_stock_for_valid_purchase():
    assert update_stock("apple", 2) is True
    assert products["apple"]["stock"] == 48


def test_update_stock_rejects_unknown_item():
    assert update_stock("chocolate", 1) is False


def test_update_stock_rejects_when_quantity_exceeds_stock():
    assert update_stock("milk", 50) is False
    assert products["milk"]["stock"] == 20
