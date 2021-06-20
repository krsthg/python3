def func_a(time_table): #마지막 수업 시작 시간
    answer = 0
    for i, t in reversed(list(enumerate(time_table))):
        if t == 1:
            answer = i
            break
    return answer

def func_b(time_table, class1, class2): #시간표, 첫수업, 마지막 수업
    answer = 0
    for i in range(class1, class2):
        if time_table[i] == 0:
            answer += 1
    return answer

def func_c(time_table):  #첫 수업 시작 시간
    answer = 0
    for i, t in enumerate(time_table):
        if t == 1:
            answer = i
            break
    return answer

def solution(time_table):
    answer = 0
    first_class = func_c(time_table) #1. 가장 첫 수업시작 시각을 구하기
    last_class = func_a(time_table) #2. 가장 마지막 수업시작 시각을 구하기
    answer = func_b(time_table, first_class, last_class) #3. 1과2 사이의 수업이 없는 시간 구하기
    return answer

time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0] #시간표
            #1: 수업시간 1시간 0:공강
ret = solution(time_table)
print("solution 함수의 반환 값은", ret, "입니다.")