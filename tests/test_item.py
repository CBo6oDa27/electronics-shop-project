"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone


test_item = Item('Jameson', 2700.0, 3)
test_item.pay_rate = 0.5

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 12", 100_000, 5, 2)


def test_item_init():
    assert test_item.price == 2700.0
    assert test_item.name == 'Jameson'
    assert test_item.quantity == 3

def test__repr__():
    assert repr(test_item) == "Item('Jameson', 2700.0, 3)"

def test__str__():
    assert str(test_item) == "Jameson"

def test_item_calculate_total_price():
    assert test_item.calculate_total_price() == 8100.0

def test__add__():
    assert phone1 + phone2 == 10


def test_item_apply_discount():
    test_item.apply_discount()
    assert test_item.price == 1350.0


def test_string_to_number():
    assert test_item.string_to_number('673.0') == 673
    assert test_item.string_to_number('200') == 200
    assert test_item.string_to_number('200.27') == 200


def test_instantiate_from_csv():
    test_item.instantiate_from_csv('../src/items.csv')
    assert len(test_item.all) == 5


def test_name():
    test_item.name = '1234567890123'
    assert test_item.name == '1234567890'

