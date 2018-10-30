
import pytest
from unittest.mock import MagicMock
from ShoppingCart import ShoppingCart


@pytest.fixture()
def shoppingCart():
    shoppingCart = ShoppingCart()
    shoppingCart.itemPrice("z", 1)
    shoppingCart.itemPrice("y", 2)
    return shoppingCart

def test_getTotal(shoppingCart):
    shoppingCart.item("z")
    assert shoppingCart.getTotal() == 1

def test_getTotalWithMultipleItems(shoppingCart):
    shoppingCart.item("z")
    shoppingCart.item("y")
    assert shoppingCart.getTotal() == 3

def test_addDiscountRule(shoppingCart):
    shoppingCart.discount("z", 3, 2)

def test_canApplyDiscountRule(shoppingCart):
    shoppingCart.discount("z", 3, 2)
    shoppingCart.item("z")
    shoppingCart.item("z")
    shoppingCart.item("z")
    assert shoppingCart.getTotal() == 2

def test_canNotApplyDiscountRule(shoppingCart):
    shoppingCart.discount("z", 3, 2)
    shoppingCart.item("z")
    assert shoppingCart.getTotal() != 2

def test_exceptionWhenNotExxistingItemAdded(shoppingCart):
    with pytest.raises(Exception):
        shoppingCart.item("x")

def test_verifyReadPricesFile(shoppingCart, monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.__iter__.return_value = ["x 3"]
    mock_open = MagicMock(return_value = mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    shoppingCart.readPricesFile("testfile")
    shoppingCart.item("x")
    result = shoppingCart.getTotal()
    mock_open.assert_called_once_with("testfile")
    assert result == 3

