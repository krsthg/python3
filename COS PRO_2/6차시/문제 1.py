def solution(temperature, A, B):
    answer = 0
    #for i in range(0, len(temperature)):
    for i in range(A+1,  B):
                #A부터 B사이의 수를 i에 하나씩 대입
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            #i가 A보다 크고 i가 B보다 크면
            answer += 1
    return answer

temperature = [3, 2, 1, 5, 4, 3, 3, 2] #n일동안 매일매일의  평균 기온 리스트
A = 1
B = 6
    #A번째 수 ~ B번째 수 사이 A와 B보다 큰 수 찾기
ret = solution(temperature, A, B)
print("solution 함수의 반환 값은", ret, "입니다.")