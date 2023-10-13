n = int(input())
m = n//100
r = (n%100)//10
k = n%10
print(n)
print(m, k, r, sep='')
print(r, m, k, sep='')
print(r, k, m, sep='')
print(k, m, r, sep='')
print(k, r, m, sep='')
