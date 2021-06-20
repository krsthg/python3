def solution(papers, K):
    length = len(papers) #인원수
    for i, paper in enumerate(papers): #필요한 종이를 하나씩 대입
        K -= paper #필요한 만큼 K에서 빼기
        if K < 0: #K가 0보다 작으면
            #length = i #K가 0미만일 경우 인원 넣기
            return i
    return length #인원

papers1 = [2, 4, 2, 3, 1]
K1 = 10
ret1 = solution(papers1, K1)
print("solution 함수의 반환 값은", ret1, "입니다.")

papers2 = [2, 4, 2, 3, 1]
K2 = 14
ret2 = solution(papers2, K2)
print("solution 함수의 반환 값은", ret2, "입니다.")