# 2525 오븐 시계

H , M = map(int, input().split())

# a = int(input())
# b = (M + a) // 60
# if ((M + a) > 60 ):
#     H = H + b
#     if(H == 23):
#         H -= 23
#     M = (M + a) - (60*b)
#     print(H, M)
# elif((M + a) < 60):
#     M = M + a
#     print(H, M)



a = int(input())  # 오븐구이에 필요한 시간 입력받기

end_hour = H  # 오븐구이 끝 시각의 시 초기값 설정
end_minute = M + a  # 오븐구이 끝 시각의 분 계산

if end_minute >= 60:  # 분이 60분을 초과하는 경우
    end_hour += end_minute // 60  # 시간에 분을 더해주기
    end_minute %= 60  # 60분을 초과한 부분은 분으로 다시 설정

if end_hour >= 24:  # 시간이 24시를 초과하는 경우
    end_hour %= 24  # 24시를 초과한 부분은 시간으로 다시 설정

print(end_hour, end_minute)  # 오븐구이 끝 시각 출력

