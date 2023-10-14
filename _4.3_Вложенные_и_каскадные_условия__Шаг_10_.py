n = int(input())
if n == 0:
    print('green')
elif 1 <= n <= 10:
    if n %2 == 0:
        print('black')
    if n % 2 != 0:
        print('red')
elif 11 <= n <= 18:
    if n % 2 == 0:
        print('red')
    if n % 2 != 0:
        print('black')
elif 19 <= n <= 28:
    if n % 2 == 0:
        print('black')
    if n % 2 != 0:
        print('red')
elif 29 <= n <= 36:
    if n % 2 == 0:
        print('red')
    if n % 2 != 0:
        print('black')
else:
    print('color error')
