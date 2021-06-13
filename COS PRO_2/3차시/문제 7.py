def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot    

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i %  4 == 0:
            #answer += 1
            answer -= 1
        i = i + 1
        
    return answer


num_apple1 = 5 #사과 개수
num_carrot1 = 1 #당근 개수
k1 = 2 #토끼를 위해 빼놓은 사과/당근 개수
ret1 = solution(num_apple1, num_carrot1, k1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10 #사과 개수
num_carrot2 = 5 #당근 개수
k2 = 4 #토끼를 위해 빼놓은 사과/당근 개수
ret2 = solution(num_apple2, num_carrot2, k2)

print("solution 함수의 반환 값은", ret2, "입니다.")

#틀린 결과: 1, 4
#수정 후 결과: 1, 2