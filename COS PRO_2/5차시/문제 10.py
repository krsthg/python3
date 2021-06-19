#import math

def solution(time_table, n):
    answer = 0
    list = [0 for _ in range(n)] #n: 인원수 만큼 반복하여 리스트 생성[초기값:0]
    for i, t in enumerate(time_table):
    #for index, value in enumertate(리스트):
        list[i%n] += t #인덱스의 인원수 만큼 나머지 구하기
    answer = max(list) #가장 많이 일한 근무시간 찾기
    return answer

time_table1 = [1, 5, 1, 9] #시간표
n1 = 3
ret1 = solution(time_table1, n1)
print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)
print("solution 함수의 반환 값은", ret2, "입니다.")