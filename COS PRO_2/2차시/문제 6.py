#문제 6
def solution(floors):
    dist  = 0
    length = len(floors)
    for i in range(len(floors)+1):
        if @@@:
            dist += floors[i] - floors[i-1]
        else:
            dist += floors[i-1]- floors[i]

floors = [1,2,5,4,2]
ret = solution(floors)

print("solution 함수의 결과:", ret)