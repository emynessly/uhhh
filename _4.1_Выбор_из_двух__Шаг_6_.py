n = int(input())
k = (n//1000) + (n%10)
l = (n%1000)//100 - (n%100)//10
if k == l:
    print('YES')
else:
    print('NO')
