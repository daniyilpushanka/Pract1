def sport():
    distance = 10
    total = 0
    days = 0

    while total < 50:
        total = total + distance
        days = days + 1
        distance = distance * 1.1

    print()
    print("Кількість днів:", days)
    print("Загальна відстань:", total)