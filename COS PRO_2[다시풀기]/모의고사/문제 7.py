def solution(height):
    dx = [-1, 1, 0, 0]
        # 서, 동, 0, 0
    dy = [0, 0, -1, 1]
        # 0, 0, 남, 북
    answer = 0
    for x in range(4):
        for y in range(4):
            check = True
            for location in range(4):
                if 0<=x+dx[location] and x+dx[location]< 4 and 0<=y+dy[location] and y+dy[location]<4:
                #지역의 가로가 0보다 크고 지역 동쪽보다 작으면 지역의 세로가 6보다 크고 세로가 남보다 작으면
                    if height[x+dx[location]][y+dy[location]] <= height[x][y]:
                    #지형[가로=서쪽,동쪽][세로=남쪽,북쪽]<= 지역
                        check = False
            if check:
                answer+=1
    return answer

height = [[3,6,2,8],[7,3,4,2],[8,6,7,3],[5,3,2,9]]
print("solution 결과:", solution(height))