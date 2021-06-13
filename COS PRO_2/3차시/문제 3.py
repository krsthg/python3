#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(scores):
    sum(scores) - max(scores) - min(scores) //len(scores)-2
    #sum(리스트): 리스트내 모든 합계
    #max(리스트): 리스트내 가장 큰 수
    #min(리스트): 리스트내 가장 작은 수
    #len(리스트): 리스트내 요소 수
        #len()-2: 가장큰수, 가장작은수 제외
    #return 값: 현재 함수를 종료 하면서 되돌려주는 값
    answer = 0
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")