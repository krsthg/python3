#문제 7   정답: or => and           +1 => +=1
def solution(scores):   #토익시험이 조건을 충족하면 초급영어강의 수강대사 구하기
    count = 0
    for s in scores:
        if 650<=s and s<800:    #토익시험 650이상 600미만
            count +=1
    return count

scores = [650,722,914,558,714,803,650,679,669,800]
ret = solution(scores)
print("solutiom 함수 결과:", ret,"명.")