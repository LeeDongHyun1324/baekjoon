# 10809번 알파벳 찾기

alpha = ['a','b','c','d','e','f','g','h','i','j',
         'k','l','m','n','o','p','q','r','s','t','u',
         'v','w','x','y','z']


s = input()

for char in alpha:
    if char in s:
        print(s.index(char), end=' ')   #s 문자열에서 처음 나온 알파벳의 인덱스 값을 구해야하기 때문에 s.index(char)로 해야함
    else:
        print('-1', end=' ')
        


# word = input()
# alpha_positions = [-1] * 26

# for i in range(len(word)):
#     index = ord(word[i]) - ord('a')
#     if alpha_positions[index] == -1:
#         alpha_positions[index] = i

# for position in alpha_positions:
#     print(position, end=' ')

