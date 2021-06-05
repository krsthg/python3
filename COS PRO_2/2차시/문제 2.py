#문제 2
def func_a(arr): #5의 배수 구하는 함수
    count = 0
    for n in arr:
        if n % 5 == 0: #값%5==0 => 5의배수
            count +=1
    return count

def func_b(three, five): #3의배수와 5의배수 개수 비교
    if three>five:      #3의배수 개수>5의배수 개수
        return "three"
    elif three<five:    #3의배수 개수<5의배수 개수
        return "five"
    else:               #3의배수 개수=5의배수 개수
        return "same"

def func_c(arr):  #3의 배수 구하는 함수
    count = 0
    for n in arr:
        if n%3 == 0: #값%3==0 => 3의배수
            count+=1
    return count

def solution(arr):
    count_three = func_c(arr)
    count_five = func_a(arr)
    answer = func_b(count_three,count_five)
    return answer

arr = [2,3,6,9,12,15,10,20,22,25]
ret = solution(arr)
print("solution 함수의 결과:", ret)