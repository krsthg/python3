#1~ ㅡ-1까지 누적합계
#1단계~2단계의 결과값
def func_a(k): #m->k        n-1->k
    sum = 0 #누적합계 변수
    for i in range(k+1):
    #for 변수 in range(~전까지):
        #i는 1부터 k전까지 반복
        #i는 1부터 k+1까지 반복
        sum += i #i를 sum에 저장
    return sum


