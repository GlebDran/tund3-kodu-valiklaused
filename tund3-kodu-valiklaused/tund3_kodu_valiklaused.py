print("\n--- ulesanne 1 ---\n")

chislo = int(input("Введите число: "))

if chislo < 0:
    print("Число отрицательное.")
elif chislo == 0:
    print("Это ноль.")
else:
    if chislo % 2 == 0:
        print("Число положительное и четное.")
    else:
        print("Число положительное и нечетное.")

print("\n--- ulesanne 2 ---\n")

a = int(input("первый угол: "))
b = int(input("второй угол: "))
c = int(input("третий угол: "))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:

    if a == b == c:
        print("Это равносторонний треугольник.")
    elif a == b or a == c or b == c:
        print("Это равнобедренный треугольник.")
    else:
        print("Это разносторонний треугольник.")
else:
    print("Это не углы треугольника.")

print("\n--- ulesanne 3 ---\n")


otvet = input("расшифровать порядковый номер дня недели? (да/нет): ")

if otvet.upper() == "ДА":
    
    day_number = int(input("Введите число от 1 до 7: "))
    if 1 <= day_number <= 7:
       
        dni = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        print(f"{dni[day_number - 1]}.")
    else:
        print("Ошибка: введите число от 1 до 7.")
elif otvet == "нет":
    print("Программа завершена.")
else:
    print("Ошибка: введите 'да' или 'нет'.")

print("\n--- ulesanne 4 ---\n")


try:
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))
    
    
    if month < 1 or month > 12:
        print("Ошибка!!! месяц должен быть от 1 до 12.")
    elif day < 1 or day > 31:
        print("Ошибка!!! день должен быть от 1 до 31.")
    elif (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30):
        print("Ошибка: в этом месяце нет такого дня.")
    else:
        if (month == 12 and day >= 22) or (month == 1 and day <= 19):
            zodiac = "Козерог"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            zodiac = "Водолей"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            zodiac = "Рыбы"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            zodiac = "Овен"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            zodiac = "Телец"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            zodiac = "Близнецы"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            zodiac = "Рак"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            zodiac = "Лев"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            zodiac = "Дева"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            zodiac = "Весы"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            zodiac = "Скорпион"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            zodiac = "Стрелец"
        
        print(f"Ваш знак зодиака: {zodiac}.")
except ValueError:
    print("Ошибка: введите числовые значения для дня и месяца.")

print("\n--- ulesanne 5 ---\n")

user_input = input("Введите значение: ")

# Проверка текста
if user_input.isalpha():
    print(f"Вы ввели текст: {user_input}")

# Проверка чисел
else:
    try:
        # Преобразуем ввод в число
        num = float(user_input)

        # Проверка на целое число
        if num.is_integer():
            result = int(num) // 2  # Целочисленное деление на 2 (50%)
            print(f"Введено целое число. 50% от него: {result}")
        else:
            result = num * 0.7  # 70% от дробного числа
            print(f"Введено дробное число. 70% от него: {result}")

    except ValueError:
        print("Ошибка: невозможно определить тип введенного значения.")
