#10811 바구니 뒤집기

N, M = map(int,input().split())

str = []

for a in range(1,N+1):
    str.append(a)

for k in range(M) :
    i, j = map(int,input().split())
    str[i-1:j] = reversed(str[i-1:j])

print(*str)