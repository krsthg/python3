def func_a(scores1, scores2): #기말고사에서 중간고사를 뺀 최댓값
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer

def func_b(scores1, scores2): #최솟값
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        #answer = min(answer, score1 - score2) #중간-기말
        answer = min(answer, score2 - score1)  #기말-중간
    return answer
            
def solution(mid_scores, final_scores): #점수
    up = func_a(mid_scores, final_scores)
    down = func_b(mid_scores, final_scores)
    answer = [up, down] #1번과 2번 과정에서 구한 점수를 리스트에 담아 return
    return answer

mid_scores = [20, 50, 40]   #중간
final_scores = [10, 50, 70] #기말
ret = solution(mid_scores, final_scores)
print("solution 함수의 반환 값은", ret, "입니다.")