def solution(scores):
    answer = 0
    answer = (sum(scores)- max(scores)-min(scores))// (len(scores)-2)
    #max(list): 최대값
    #min(list): 최솟값
    #len(list): 개수
    #sum(list): 총합
    return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
scores2 = [1,1,1,1,1]
print("solution 결과:", solution(scores1))
print("solution 결과:", solution(scores2))