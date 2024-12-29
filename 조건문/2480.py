#2480 주사위 세개

dice = list(map(int, input().split()))

result = 0

if (dice[0] == dice[1] == dice[2]):
    result = 10000 + 1000*dice[0]
elif(dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]):
    if(dice[0] == dice[1] or dice[1] == dice[2]):
        result = 1000 + 100*dice[1]
    else:
        result = 1000 + 100*dice[2]
else:
    result = 100*max(dice)

print(result)

