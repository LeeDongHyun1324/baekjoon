#11720 숫자의 합

# 숫자의 개수 N 입력받기
N = int(input())

# N개의 숫자를 공백 없이 입력받아서 모두 합하기
numbers = input()   #입력받은 값의 형태가 안정해져 있으면 str
total_sum = 0
for i in range(N):
    total_sum += int(numbers[i])    #str일 때는 배열처럼 생각해서 인덱스로 나누기 가능

# 결과 출력
print(total_sum)
