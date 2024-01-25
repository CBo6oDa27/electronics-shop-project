import pytest

from src.phone import Phone

@pytest.fixture
def phone_test():
    return Phone("Nokia", 27000, 2, 2)
def test_phone_init(phone_test):
    assert phone_test.name == 'Nokia'
    assert phone_test.price == 27000
    assert phone_test.quantity == 2
    assert phone_test.number_of_sim == 2