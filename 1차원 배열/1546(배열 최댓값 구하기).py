#1546 평균

N = int(input())

arr = list(map(int,input().split()))
max = arr[0]

for i in range(N):          #최대값 max 구하는 방법
    if (max < arr[i]):
        max = arr[i]

arr_avg = []                #
sum = 0
for j in range(N):
    arr_avg.append(arr[j] / max * 100)
    sum += arr_avg[j]

avg = sum/len(arr)
print(avg)
