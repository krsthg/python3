def solution(day, numbers):
    count = 0
    for number in numbers:
        #if number%2 != day%2: #만약 차번호의 나머지가 날자의 나머지와 같지 않을 경우
        if number%2 == day%2:  #                                같을 경우
            count += 1
    return count

day = 17 #몇일인지를 나타내는 변수
numbers = [3285, 1724, 4438, 2988, 3131, 2998] #차번호
ret = solution(day, numbers)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

#틀린 결과: 4
#수정 후 결과: 2