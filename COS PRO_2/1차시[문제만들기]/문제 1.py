#문제 1
    #조건1: 리스트에 사이즈별로 개수를 담아서 리턴해주는 함수
def solution(T): #함수 만들기
    T2 = [0, 0, 0, 0, 0, 0] #1. 티셔츠 사이즈별 개수를 담을 리스트 선언
                # XS, S, M, L, XL, XXL
    for ss in T: #리스트 반복 => 리스트내 항목이 변수에 하나씩 대입
        if ss == "XS":              #2. 만약에 XS이면 첫번째 인덱스 +1
            T2[0] += 1
        if ss == "S":
            T2[1] += 1
        if ss == "M":
            T2[2] += 1
        if ss == "L":
            T2[3] += 1
        if ss == "XL":
            T2[4] += 1
        if ss == "XXL":
            T2[5] += 1
    return T2
shirt_size = ["XS","S","L","L","XL","S"]
ret = solution(shirt_size)
print(ret)
#-----------------------------
def solution(S): #함수 만들기
    S2 = [0, 0, 0, 0, 0, 0]
    for ss in S:
        if ss == 8: #1학년이면
            S2[0] += 1
        if ss == 9: #2학년이면
            S2[1] += 1
        if ss == 10: #3학년이면
            S2[2] += 1
        if ss == 11: #4학년이면
            S2[3] += 1
        if ss == 12: #5학년이면
            S2[4] += 1
        if ss == 13: #6학년이면
            S2[5] += 1
    return S2

S = [8,8,9,10,10,11,9,8,12,13,8,11]
ret = solution(S)
print("초등학생 인원수:", ret)
#-----------------------------
def a(number):
    N=[0,0]
    for a in number:
        if a%2== 0 and a>99 :
            N[0] +=1
        elif a%2==1 and a>99:
            N[1] +=1
    return N

number = [1, 2,34 ,5234, 123,4, 546,1451,34531456 ,6123,2,1234,45,5,1234,123]
ret = a(number)
print(ret)
#----------------------------- 문자가 목록에서 서로 다른 문자가 몇개 있는지 출력
def b(단어, 목록):
    다른문자 = [0,0,0]

    w= 0
    for q in 목록:
        count = 0
        for b in range(17):
            print(q[b])
            if 단어[b] != q[b]:
                count += 1
        다른문자[w] = count
        w += 1

    return 다른문자


단어 = 'anticonstitutiona'
목록 = ['aatitonstinuional', 'bnticonstiqtioall', 'abticonsfitnlonol']

ret = b(단어, 목록)
print(ret)