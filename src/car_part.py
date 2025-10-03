class CarPart:
    PART_MULTIPLIERS = {
        "капот": 1.0,
        "передняя дверь": 1.2,
        "задняя дверь": 1.1,
        "передний бампер": 1.0,
        "задний бампер": 1.0,
        "крыша": 1.1,
    }

    def __init__(self, name: str):
        self.name = name.lower()
        self.multiplier = self.PART_MULTIPLIERS.get(self.name, 1.0)