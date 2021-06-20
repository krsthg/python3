#import math

def solution(people):
    answer = [0 for _ in range(4)] #0을 4개 가지고 있는 리스트
    for size in people:
        if size<95: #사이즈가 95 미만
            answer[0] +=1 #리스트[0] = S의 개수에 1추가
        elif 95<=size<100: #사이즈가 90 이상 100 미만
            answer[1]+=1 #리스트[1] = S의 개수에 1추가
        elif 100<=size<105: #사이즈가 100 이상 105 미만
            answer[2]+=1 #리스트[2] = S의 개수에 1추가
        elif size>=105: #사이즈가 105 이상
            answer[3]+=1 #리스트[3] = S의 개수에 1추가
    return answer

people = [97, 102, 93, 100, 107] #주문 사이즈
ret = solution(people)
print("solution 함수의 반환 값은 ", ret, " 입니다.")