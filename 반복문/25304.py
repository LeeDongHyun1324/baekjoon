#25304 영수증

a = int(input())

b = int(input())
value = []
for i in range(b):
    c, d = map(int, input().split())
    value.append(c*d)

sum = sum(value)

if (sum == a):
    print("Yes")
else:
    print("No")