# import math
def solution(scores, cutline):
    answer = 0
    for score in scores: #점수리스트를 하나씩 점수에 넣기
        if score >= cutline: #해당 점수가 커트라인보다 높으면
            answer +=1 #합격자수 1 씩 증가
    return answer

scores = [80, 90, 55, 60, 59] #학생들 점수 리스트
cutline = 60 #커트라인[합격기준]
ret = solution(scores, cutline)
              #점수리스트, 커트라인
print("solution 함수의 반환 값은", ret, "입니다.")