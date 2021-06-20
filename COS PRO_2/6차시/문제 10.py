def solution(weight, boxes):
    answer = 0
    for x in boxes:
        if 540<=x*1.1 <= 660:
            answer += 1
    return answer

weight = 600
boxes = [653, 670, 533, 540, 660]
ret = solution(weight, boxes)
print("solution 함수의 반환 값은", ret, "입니다.")