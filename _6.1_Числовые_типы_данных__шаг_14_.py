n = int(input())
m = n//100
k = (n%100)//10
l = n%10
if (max(m, k, l)-min(m, k, l)) == ((k+l+m)-(max(m, k, l)+min(m, k, l))):
    print('Interesting number')
else:
    print('Uniteresting number')
