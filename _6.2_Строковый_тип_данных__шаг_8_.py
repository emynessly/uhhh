n = input()
m = input()
k = input()
a = len(n)
b = len(m)
c = len(k)
if a == min(a, b, c):
    print(n)
elif b == min(a, b, c):
    print(m)
elif c == min(a, b, c):
    print(k)
if a == max(a, b, c):
    print(n)
elif b == max(a, b, c):
    print(m)
elif c == max(a, b, c):
    print(k)
