def solution (scores):
    answer = 0
    for i in scores:
        if i>= cutline:
            answer += 1
    return answer

scores = [80,90,55,60,59]
cutline = 60
print("solution 결과:", solution(scores))