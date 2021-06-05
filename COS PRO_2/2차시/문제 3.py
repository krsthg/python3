#문제 3
import math

def solution(N,M):
    total = 0
    for i in range(N, M+1): #4부터 8전까지 1씩 증가
        if i %2==0: # ==0: 짝수       ==1: 홀수
            total += i*i #수*수 = 제곱
    return total

N = 4   #4 5[홀수] 6 7[홀수]
M = 7
        #4*4 = 16   6*6 = 36    16+36 = 52
ret = solution(N,M)
print("solution 함수의 결과:",ret)