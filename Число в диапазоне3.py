import random

hiDiapazon = 0
lowDiapazon = 0
x = 0
y = 1
n = 0
game = True
play = True
count = 0

while game:
    print("Введите x и y, где x < y")

    while play:

        x = ""
        y = ""
        while not x.isdigit():
            x = input("Введите х: ")
            if not x.isdigit():
                print("." * 27 + "Введите, пожалуйста, целое число x: ")
        while not y.isdigit():
            y = input("Введите y: ")
            if not y.isdigit():
                print("." * 27 + "Введите, пожалуйста, целое число y: ")

        x = int(x)
        y = int(y)

        if x < y:
            count += 1
            hiDiapazon = y
            lowDiapazon = x

            n = random.randint(lowDiapazon + 1, hiDiapazon - 1)
            if n % 5 == 0:
                print(f"{x} < {n} < {y}")
            else:
                print("0")

            print(f"Количество попыток {count}")

            if (input("Enter - сыграть ещё, 0 - выход ") == "0"):
                play = False
            else:
                play = True
        else:
            print("x > y")
            play = False

    game = False

print("До свидания!")
