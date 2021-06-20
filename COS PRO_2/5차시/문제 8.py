def solution(usage):
    answer = 0
    if usage > 30: #상수도 30 초과이면
        # answer = 20 * 430 + 10 * 570 + (usage - 20) * 840
        #          20톤 가격, 10톤 가격, 20톤을 뺀 * 840
        answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
                 #1단계 가격, 2단계 가격, 3단계 가격
    elif usage > 20: #상수도 20 초과이면
        answer = 20 * 430 + (usage - 20) * 570
                #1단계 가격, 2단계 가격
    else: #그 외 상수도 20이하
        answer = usage * 430
                #1단계 가격
    return answer

usage = 35
ret = solution(usage)
print("solution 함수의 반환 값은", ret, "입니다.")