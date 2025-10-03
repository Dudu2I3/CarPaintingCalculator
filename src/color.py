class Color:
    """Класс цвета: name и multiplier."""
    COLOR_MULTIPLIERS = {
        "белый": 1.0,
        "синий": 1.0,
        "жёлтый": 1.1,
        "жёлтый": 1.1,   # учтены варианты
        "красный": 1.0,
        "перламутровый": 1.2,
        "серый металлик": 1.3,
    }

    def __init__(self, name: str):
        self.name = name.lower()
        self.multiplier = self.COLOR_MULTIPLIERS.get(self.name, 1.0)