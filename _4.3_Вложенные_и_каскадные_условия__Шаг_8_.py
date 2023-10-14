n = int(input())
m = int(input())
r = input()
if (r == '*') or (r == '-') or (r == '+') or (r == '/'):
    if r == '*':
        print(n * m)
    if r == '+':
        print(n + m)
    if r == '-':
        print(n - m)
    if m == 0 and r == '/':
        print('You cant divide by zero!')
    if m != 0 and r == '/':
        print(n / m)   
else:
    print('Invalid operation')
