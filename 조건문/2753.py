#2753 윤년

a = int(input())
b = a % 4
c = a % 400 
d = a % 100

if (((b == 0) and  (d != 0)) or (c == 0)):
    print("1")
else:
    print("0")
