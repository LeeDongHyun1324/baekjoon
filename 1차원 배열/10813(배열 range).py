#10813 공 바꾸기

n , m = map(int,input().split())

arr = list(range(1,n+1))

for i in range(m):
    k , l = map(int,input().split())
    # temp = arr[l - 1]
    # arr[l - 1] = arr[k - 1]
    # arr[k - 1] = temp
    arr[l - 1], arr[k - 1] = arr[k - 1], arr[l -1]

print(*arr)
    









