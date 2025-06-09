def area(num1, num2):
    return num1 * num2


while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        print("Результат сложения этих чисел:", num1 + num2)
        print("Площадь (произведение этих чисел):", area(num1, num2))
    except ValueError:
        print("Ошибка: введите корректные числа.")