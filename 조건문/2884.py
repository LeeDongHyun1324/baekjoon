# 2884 알람 시계

H, M= map(int,input().split())

if (M >= 45):
    M = M - 45
    print(H, M)
elif(M < 45):
    if(H == 0):
        H = H + 23
    else:
        H = H - 1
    M = M + 15
    print(H, M)
    