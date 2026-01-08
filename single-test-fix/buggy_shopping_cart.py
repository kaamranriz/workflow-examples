"""
Shopping Cart module with intentional bugs for testing the Run & Fix Single Test workflow.
The bugs should be detected by the test file and fixed by the workflow.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class Product:
    """Represents a product in the store."""
    id: str
    name: str
    price: float
    quantity_in_stock: int


class ShoppingCart:
    """Shopping cart with intentional bugs to be fixed."""

    def __init__(self):
        self.items: Dict[str, int] = {}  # product_id -> quantity
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        """Add a product to the catalog."""
        self.products[product.id] = product

    def add_to_cart(self, product_id: str, quantity: int = 1) -> bool:
        """Add item to cart. Returns True if successful."""
        if product_id not in self.products:
            return False

        product = self.products[product_id]
        current_qty = self.items.get(product_id, 0)

        # BUG 1: Should check if requested quantity is available
        # Currently allows adding more than available stock
        self.items[product_id] = current_qty + quantity
        return True

    def remove_from_cart(self, product_id: str, quantity: int = 1) -> bool:
        """Remove item from cart. Returns True if successful."""
        if product_id not in self.items:
            return False

        current_qty = self.items[product_id]

        # BUG 2: Off-by-one error - should be >= not >
        if quantity > current_qty:
            del self.items[product_id]
        else:
            self.items[product_id] = current_qty - quantity
        return True

    def get_cart_total(self) -> float:
        """Calculate total price of items in cart."""
        total = 0.0
        for product_id, quantity in self.items.items():
            product = self.products.get(product_id)
            if product:
                # BUG 3: Should multiply by quantity
                total += product.price
        return total

    def get_item_count(self) -> int:
        """Get total number of items in cart."""
        # BUG 4: Returns number of unique products instead of total items
        return len(self.items)

    def apply_discount(self, percentage: float) -> float:
        """Apply a percentage discount to the cart total."""
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100")

        total = self.get_cart_total()
        # BUG 5: Adds discount instead of subtracting
        discount = total * (percentage / 100)
        return total + discount

    def clear_cart(self) -> None:
        """Empty the shopping cart."""
        self.items = {}

    def checkout(self) -> Optional[Dict]:
        """Process checkout and return order summary."""
        if not self.items:
            return None

        order = {
            "items": [],
            "total": self.get_cart_total(),
            "item_count": self.get_item_count()
        }

        for product_id, quantity in self.items.items():
            product = self.products.get(product_id)
            if product:
                order["items"].append({
                    "name": product.name,
                    "quantity": quantity,
                    "price": product.price,
                    "subtotal": product.price * quantity
                })

        self.clear_cart()
        return order


