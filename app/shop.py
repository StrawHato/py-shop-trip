import json
from typing import Any
from app.customer import Customer, CONFIG_PATH


with open(CONFIG_PATH, "r") as file:
    config = json.load(file)
    shops = config["shops"]


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __getitem__(self, item: str) -> Any:
        if item in self.products:
            return self.products[item]
        if hasattr(self, item):
            return getattr(self, item)
        raise KeyError(item)

    def products_cost(self, customer: Customer) -> float:
        total = 0
        for product, quanty in customer.product_cart.items():
            price = self.products.get(product) * quanty
            total += price
        return total
