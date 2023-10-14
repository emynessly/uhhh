n = int(input())
m = int(input())
k = int(input())
if (n > m and n < k) or (n < m and n > k):
    print(n)
elif (m > n and m < k) or (m < n and m > k):
    print(m)
elif (k > m and k < n) or (k < m and k > n):
    print(k)
