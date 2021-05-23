#문제 2
def solution(price, grade): #함수
    answer = 0

    if grade == "S":
        answer = price *0.95  #1:100%       0.5:50%     0.25:25%
    if grade == "G":
        answer = price *0.9
    if grade == "V":
        answer = price *0.85

    return int(answer)
price1 = 2500
grade1 = "V"
ret1 = solution(price1,grade1) #함수 호출

print("Solution: return value of thr function is", ret1,".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2,grade2)

print("Solution: return value of thr function is", ret2,".")