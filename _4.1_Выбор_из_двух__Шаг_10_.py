n = int(input())
m = int(input())
k = int(input())
l = int(input())
if n <= m:
    x = n
else:
    x = m
if k <= l:
    y = k
else:
    y = l
if x <= y:
    print(x)
else:
    print(y)
