n = int(input())
m = int(input())
k = int(input())
if (n>m and n>k and n < (m+k)) or (k>m and k>n and k < (m+n)) or (m>n and m>k and m < (n+k)):
    print('YES')
else:
    print('NO')
