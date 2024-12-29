# 3052 나머지

# arr = []
# arr1 = []
# for i in range(10):
#     arr.append(int(input()))
#     arr1.append(arr[i] % 42)

remainders = set()  # 서로 다른 나머지를 기록할 집합(set)
for _ in range(10):
    num = int(input())
    remainder = num % 42
    remainders.add(remainder)

count = len(remainders)  # 서로 다른 나머지의 개수

print(count)

