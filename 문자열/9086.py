#9086 문자열

n = int(input())

S = []

for i in range(n):          #S문자열에 n만큼 입력한 문자열 넣기
    S.append(str(input()))

for j in range(n):
    index = S[j]
    print(f"{index[0]}{index[-1]}")

