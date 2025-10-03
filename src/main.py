from calculator import Calculator

def main():
    calc = Calculator()
    part = input("Введите название детали: ").strip()
    color = input("Введите цвет: ").strip()
    discount_input = input("Введите скидку (%) или оставьте пустым: ").strip()

    if discount_input:
        price = calc.calculate_with_discount(part, color, float(discount_input))
        print(f"Стоимость покраски со скидкой: {price} руб.")
    else:
        price = calc.calculate(part, color)
        print(f"Стоимость покраски: {price} руб.")

if name == "__main__":
    main()