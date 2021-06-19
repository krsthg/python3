#import math

def solution(score):
    answer = [0] * len(score) #점수 개수만큼 리스트
    #리스트[0] 인덱스 점수 개수만큼 0 넣기
    for i in range(len(score)):
        answer[i] = sum(map(lambda X:X > score[i], score))+1
        #lambda: 람다식[이름없는 함수]
        #lambda 인수: 표현식

        #형태: (lambda x, y: x+y)(10,20)
                  #인수1, 인수2

        #함수 형태: def 함수(x, y):
        #               return x+y
        #         함수(10,20)
    return answer

score1 = [90, 87, 87, 23, 35, 28, 12, 46] #점수 리스트
ret1 = solution(score1)
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)
print("solution 함수의 반환 값은 ", ret2, " 입니다.")