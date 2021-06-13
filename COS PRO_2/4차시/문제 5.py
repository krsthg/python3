def solution(calorie):
    #min_cal = 0
    min_cal = 1000 #모든 열량 중 가장 큰 수의 임의의 값 => 873보다 큰 값
    answer = 0
    for cal in calorie: #모든 열량을 하나씩 cal에 대입
        if cal > min_cal: #현재 열량이 최소열량보다 작으면
            answer += cal - min_cal #현재열량 - 10000
        min_cal = min(min_cal, cal) #최소열량과 현재열량중 작은값 : 최소열량
    return answer

calorie = [713, 665, 873, 500, 751] #열량
          #1날, 2날 ,3날, 4날, 5날
          #전날보다 더 많이 먹었을 경우 운동
          #1, 2, 4날 운동:X
          #3, 5날:O
ret = solution(calorie)
print("solution 함수의 반환 값은", ret, "입니다.")