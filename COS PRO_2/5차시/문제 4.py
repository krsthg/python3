def solution(taekwondo, running, shooting):
    answer = 0
    if taekwondo >= 25: #태권도가 25이상이면
    	answer += 250 #250점 더하기
    else:
    	answer += taekwondo * 8 #경기당 8점
    answer += 250 + (60 - running) * 5 #235점
    count = 0 #10점 개수 변수
    for s in shooting:
    	answer += s
    	if s == 10: #10점이면
    		count += 1 #10점 개수
    if count >= 7: #10점이 7개 이상
    	answer += 100 #추가점수 100점
    return answer

taekwondo = 27 #25경기 이상이면 250점
running = 63 #60초 완주시 250점
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10] #더한 값[추가 100점]
ret = solution(taekwondo, running, shooting)
print("solution 함수의 반환 값은", ret, "입니다.")