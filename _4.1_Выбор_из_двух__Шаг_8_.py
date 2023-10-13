num1 = int(input())
num2 = int(input())
num3 = int(input())
d = num2 - num1  # Таким образом узнаём шаг
f1 = num1 + d == num2  # Функция номер 1
f2 = num2 + d == num3  #  Функция номер 2
if f1 & f2:  # Если выполняется функция номер 1 И функция номер 2, тогда выводит YES
    print('YES')
else:
    print('NO')
