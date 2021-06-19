def solution(point):
    answer = 0
    # if point < 1000:
    #     return 0
    # return point -(point//100)
    if point >= 1000:
        answer = point-point%100 #10의 자리 없애기
    return answer

point = 2323
ret = solution(point)
print("solution 함수의 반환 값은", ret, "입니다.")