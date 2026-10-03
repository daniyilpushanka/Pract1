from formula import calculate
from sport import sport


while True:

    print()
    print("1 - Обчислити значення виразу")
    print()
    print("2 - Визначити кількість днів")
    print()

    choice = int(input("Виберіть функцію: "))

    if choice == 1:
        print()

        x = float(input("Введіть x: "))
        y = float(input("Введіть y: "))

        result = calculate(x, y)

        print()
        print("Результат:", result)

    elif choice == 2:
        print()

        sport()

    else:
        print()
        print("Неправильний вибір")

    input("Натисніть Enter, щоб повернутися до меню")