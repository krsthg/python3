#import math

def solution(height):
    count = 0
    dx = [-1, 1, 0, 0] #가로축
    dy = [0, 0, -1, 1] #세로축
    for i in range(4): #4번 반복
        for j in range(4): #4번 반복
            d = True
            for k in range(4): #4번 반복
                if 0 <=i+dx[k] and i+ dx[k] <4 and 0<= j+ dy[k] and j+ dy[k]<4:
                    if height[i+dx[k]][j+dy[k]] <= height[i][j]:
                        d = False
            if d:
                count+=1
    return count

height = [[3, 6, 2, 8], #3, 2
          [7, 3, 4, 2], #3, 2
          [8, 6, 7, 3],
          [5, 3, 2, 9]] #2
#현재 수 기준으로 오른쪽[동] 왼쪽[서] 아래[남] 위[북] 수가 더 클 경우 => 위험지역
#2차원 리스트[[첫번째 줄], [두번째 줄], [세번째 줄], [네번째 줄]]
ret = solution(height)
print("solution 함수의 반환 값은", ret, "입니다.")