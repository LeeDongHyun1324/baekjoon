#10871 X보다 작은 수

n , x = map(int,input().split()) 


arr = list(map(int,input().split()))
result = []
for i in range(n):
    if (arr[i] < x):
        result.append(arr[i])

print(" ".join(map(str, result)))
