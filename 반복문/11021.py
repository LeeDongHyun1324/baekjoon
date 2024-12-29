# 11021 A+B-7
import sys
a = int(input())

for i in range(a):
    b, c = map(int,sys.stdin.readline().rstrip().split())
    print("Case #{}: {}".format(i + 1,b + c))