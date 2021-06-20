def solution(speed, cars):
    answer = 0
    for x in cars: #자동차들의 속도를 하나씩 x에 대입
        if x >= speed * 11 / 10 and x < speed * 12 / 10: #규정속도 100보다 10%이상 20%미만
            answer += 3 #3만원
        elif x >=  speed *1.2 and x < speed*1.3 : #규정속도 100보다 20%이상 30%미만
            answer += 5 #5만원
        elif x >= speed*1.3: #규정속도 100보다 30%이상
            answer += 7 #7만원
    return answer

speed = 100
cars = [110, 98, 125, 148, 120, 112, 89] #자동차들의 속도
#위반:    3,  0,   5,   7,   5,    3,  0 =>23만원
ret = solution(speed, cars)
print("solution 함수의 반환 값은", ret, "입니다.")