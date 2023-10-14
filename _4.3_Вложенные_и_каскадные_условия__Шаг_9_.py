n = input()
m = input()
if (n == 'red' and m == 'blue') or (m == 'red' and n == 'blue'):
    print('purple')
elif (n == 'yellow' and m == 'blue') or (m == 'yellow' and n == 'blue'):
    print('green')
elif (n == 'red' and m == 'yellow') or (m == 'red' and n == 'yellow'):
    print('orange')
elif (n == 'red' and m == 'red'):
    print('red')
elif (n == 'blue' and m == 'blue'):
    print('blue')
elif (n == 'yellow' and m == 'yellow'):
    print('yellow')
else:
    print('color error')
