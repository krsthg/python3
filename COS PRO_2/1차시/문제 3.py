#문제 3
def func_a(month, day):
    month_list = [31,28,31,30,31,30,31,31,30,31,30,31] #각 월의 마지막날
    total = 0;
    for i in range(month-1): #월-1 만큼 반복하기
        total += month_list[1] #입력한 월의 전 월까지의 일수 다 더하기
    total += day #내가 입력한 월의 일수 더하기
    #총 1월 1일부터 내가 입력한 날짜까지의 일수들 구하기
    return total-1 #하루 제외

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month,start_day) #시작날짜
    end_total = func_a(end_month, end_day) #끝날짜
    return end_total - start_total #끝날짜 - 시작날짜

start_month = 1 #시작날짜의 월
start_day = 2 #시작날짜의 일
end_month = 2 #끝나는 날짜의 월
end_day = 2 #끝나는 날짜의 일
ret = solution(start_month,start_day,end_month,end_day)
            #함수 불러내기 => 시작날짜와 끝나는 날짜를 넣어주기
print("Solution: return value of the function is", ret,".")