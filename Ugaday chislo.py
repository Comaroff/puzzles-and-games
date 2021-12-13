import random       # Для генерации случайного числа

lowDigit = 10       # Нижняя граница случайного числа
highDigit = 50      # Верхняя граница случайного числа
digit = 0           # Загаданное компьютером число

countInput = 0      # Количество попыток угадать
win = False         # Угадал текущее число?
playGame = True     # Продолжается ли игра?
x = 0               # Число, которое вводит пользователь
startScore = 100    # Начальное количество очков
score = 0           # Текущее количество очков
maxScore = 0        # Максимальное за сессию игры

# ==================================================



# ----------------- MainLoop (главный цикл)

while (playGame):
    digit = random.randint(lowDigit, highDigit)
    countInput = 0
    score = startScore
    print("Компьютер загадал число, попробуйте отгадать!")
    # ------------------- ВНУТРЕННИЙ ЦИКЛ
    while (not win and score > 0):
        print(f"Заработано очков: {score}")
        print(f"Рекорд: {maxScore}")

        x = ""
        while not x.isdigit():                                          # Пока в строке не число:
            x = input(f"Введите число от {lowDigit} до {highDigit}: ")
            if (random.randint(0, 100) < 5):
                print("Ой, всё! Я перезагадал число!")
                digit = random.randint(lowDigit, highDigit)
                print(f"Загаданное число: {digit}")
            if not x.isdigit():
                print("." * 27 + "Введите, пожалуйста,  число: ")

        x = int(x)
        if (x == digit):
            win = True
        else:
            length = abs(x - digit)
            if (length < 3):
                print("Очень горячо!")
            elif (length < 5):
                print("Горячо!")
            elif (length < 10):
                print("Тепло!")
            elif (length < 15):
                print("Прохладно!")
            elif (length < 20):
                print("Холодно!")
            else:
                print("Ледяной ветер!")

            if (countInput == 7):
                score -= 10
                if (digit % 2 == 0):
                    print("Число четное")
                else:
                    print("Число нечетное")
            elif (countInput == 6):
                score -= 8
                if (digit % 3 == 0):
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")

            elif (countInput == 5):
                score -= 4
                if (digit % 4 == 0):
                    print("Число четное")
                else:
                    print("Число не делится на 4")

            elif 2 < countInput < 5:
                score -= 2
                if (x > digit):
                    print("Загаданное число МЕНЬШЕ вашего")
                else:
                    print("Загаданное число БОЛЬШЕ вашего")
            score -= 5
        countInput += 1


    if x == digit:
        print("""Победа! Поздравляем!
        Спасибо, что сыграли!""")
    else:
        print("Ой, у вас закончились очки")

    if (input("Enter - сыграть ещё, 0 - выход ") == "0"):
        playGame = False
    else:
        win = False

    if score > maxScore:
        maxScore = score

print("До новых встреч!")







