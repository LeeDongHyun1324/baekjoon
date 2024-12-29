#5597 과제 안 내신 분..?



arr1 = []
for _ in range(28):
    arr1.append(int(input()))           #arr1에 28개의 숫자 입력

arr = []
for j in range(1, 31):
   if j not in arr1:
       arr.append(j)

print(min(arr))
print(max(arr))







