def solution(N,M):
    answer = 0
    for i in range(N,M+1):
        if i %2==0:
            answer += i*i
    return answer

N= 4
M = 7
print("solution 결과:", solution(N,M))