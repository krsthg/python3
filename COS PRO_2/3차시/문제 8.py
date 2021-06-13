def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1
    
    for i in used_tv:
        # if i >= 1: #티비 1대 이상을 틀 경우
        if i >= 2: #티비 2대 이상을 틀 경우
            answer = answer + 1
    return answer

programs = [[1, 6], [3, 5], [2, 8]] #프로그램이 시작되는 시간, 끝나는 시간
ret = solution(programs)

print("solution 함수의 반환 값은", ret, "입니다.")

#틀린 결과: 7
#수정 후 결과: 4