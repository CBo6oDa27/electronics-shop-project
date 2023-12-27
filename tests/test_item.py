"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

test_item = Item('Jameson', 2700.0, 3)
test_item.pay_rate = 0.5
def test_item_init():
    assert test_item.price == 2700.0
    assert test_item.name == 'Jameson'
    assert test_item.quantity == 3

def test_item_calculate_total_price():
    assert test_item.calculate_total_price() == 8100.0

def test_item_apply_discount():
    test_item.apply_discount()
    assert test_item.price == 1350.0



