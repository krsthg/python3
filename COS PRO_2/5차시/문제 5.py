def solution(a, b):
    answer = 0
    for i in range(1, b + 1):
        if (a * i) % b == 0: #a*b가 b의 배수가 될때 찾기
            #answer = b * i => 오답
            answer = a * i #i가 3일때
            break
    return answer

a = 4 #4일장
b = 6 #6일장
#4일장, 6일장이 동시에 열리는 날 구하기[공배수] => 12, 24, 36 ...
ret = solution(a, b)
print("solution 함수의 반환 값은", ret, "입니다.")