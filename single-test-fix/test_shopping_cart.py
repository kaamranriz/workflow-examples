"""
Test file for ShoppingCart - these tests will fail due to bugs in the source.
The Run & Fix Single Test workflow should fix the bugs in buggy_shopping_cart.py
"""

import pytest
from buggy_shopping_cart import ShoppingCart, Product


@pytest.fixture
def cart():
    """Create a shopping cart with some products."""
    cart = ShoppingCart()
    cart.add_product(Product("apple", "Apple", 1.50, 10))
    cart.add_product(Product("banana", "Banana", 0.75, 15))
    cart.add_product(Product("orange", "Orange", 2.00, 5))
    return cart


class TestShoppingCart:
    """Test cases for ShoppingCart class."""

    def test_add_to_cart_basic(self, cart):
        """Test adding items to cart."""
        assert cart.add_to_cart("apple", 2)
        assert cart.items["apple"] == 2

    def test_add_to_cart_invalid_product(self, cart):
        """Test adding non-existent product."""
        assert not cart.add_to_cart("mango")

    def test_add_to_cart_exceeds_stock(self, cart):
        """Test that adding more than available stock fails."""
        # BUG: This should return False when exceeding stock
        result = cart.add_to_cart("orange", 10)  # Only 5 in stock
        assert not result, "Should not allow adding more than available stock"

    def test_remove_from_cart(self, cart):
        """Test removing items from cart."""
        cart.add_to_cart("apple", 5)
        cart.remove_from_cart("apple", 2)
        assert cart.items["apple"] == 3

    def test_remove_exact_quantity(self, cart):
        """Test removing exact quantity removes item from cart."""
        cart.add_to_cart("banana", 3)
        cart.remove_from_cart("banana", 3)
        # BUG: Should remove the item completely when quantity reaches 0
        assert "banana" not in cart.items

    def test_get_cart_total_single_item(self, cart):
        """Test cart total with one item type."""
        cart.add_to_cart("apple", 3)
        # BUG: Total should be 3 * 1.50 = 4.50
        assert cart.get_cart_total() == 4.50

    def test_get_cart_total_multiple_items(self, cart):
        """Test cart total with multiple item types."""
        cart.add_to_cart("apple", 2)   # 2 * 1.50 = 3.00
        cart.add_to_cart("banana", 4)  # 4 * 0.75 = 3.00
        cart.add_to_cart("orange", 1)  # 1 * 2.00 = 2.00
        # Total should be 8.00
        assert cart.get_cart_total() == 8.00

    def test_get_item_count(self, cart):
        """Test counting total items in cart."""
        cart.add_to_cart("apple", 3)
        cart.add_to_cart("banana", 2)
        # BUG: Should return 5 (total items), not 2 (unique products)
        assert cart.get_item_count() == 5

    def test_apply_discount(self, cart):
        """Test applying discount to cart."""
        cart.add_to_cart("orange", 2)  # 2 * 2.00 = 4.00
        discounted = cart.apply_discount(25)  # 25% off
        # BUG: Should be 4.00 - 1.00 = 3.00
        assert discounted == 3.00

    def test_apply_discount_zero(self, cart):
        """Test applying 0% discount."""
        cart.add_to_cart("apple", 2)  # 2 * 1.50 = 3.00
        discounted = cart.apply_discount(0)
        assert discounted == 3.00

    def test_apply_discount_invalid(self, cart):
        """Test applying invalid discount raises error."""
        with pytest.raises(ValueError):
            cart.apply_discount(150)

    def test_clear_cart(self, cart):
        """Test clearing the cart."""
        cart.add_to_cart("apple", 2)
        cart.add_to_cart("banana", 3)
        cart.clear_cart()
        assert len(cart.items) == 0

    def test_checkout_empty_cart(self, cart):
        """Test checkout with empty cart returns None."""
        assert cart.checkout() is None

    def test_checkout_with_items(self, cart):
        """Test checkout with items returns order summary."""
        cart.add_to_cart("apple", 2)
        cart.add_to_cart("orange", 1)
        order = cart.checkout()

        assert order is not None
        assert len(order["items"]) == 2
        # Cart should be empty after checkout
        assert len(cart.items) == 0


