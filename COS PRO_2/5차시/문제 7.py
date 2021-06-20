def solution(stuffs):
    answer = 0
    small_counter, general_counter = 0, 0
    for s in stuffs: #손님들의 물건 구매 수
        if s > 3: #3초과
            general_counter += s #일반 계산대 +1
        else: #아니면
            small_counter += s #소량 계산대 +1
    #if small_counter > general_counter: => 오답
    if small_counter > general_counter:
        answer = small_counter
    else:
        answer = general_counter
    return answer

stuffs = [5, 3, 4, 2, 3, 2] #손님들의 물건 구매수
ret = solution(stuffs)
print("solution 함수의 반환 값은 ", ret, " 입니다.")