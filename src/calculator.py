from .car_part import CarPart
from .color import Color

BASE_PRICE = 12000.0

class Calculator:
    def __init__(self, base_price: float = BASE_PRICE):
        self.base_price = base_price

    def calculate(self, part_name: str, color_name: str) -> float:
        part = CarPart(part_name)
        color = Color(color_name)
        price = self.base_price * part.multiplier * color.multiplier
        return round(price, 3)

    def calculate_with_discount(self, part_name: str, color_name: str, discount: float) -> float:
        price = self.calculate(part_name, color_name)
        final_price = price * (1 - discount / 100)
        return round(final_price, 2)