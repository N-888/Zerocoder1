while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print("Результат умножения этих чисел:", num1 + num2)
    except ValueError:
        user_input = input("Ошибка: Введите корректные числа.")