def solution(time_table, worker):
    answer = 0
    list = [0 for _ in range(worker)]
            #근무자수 만큼 0의 개수를 리스트에 저장
    for x, y in enumerate(time_table):
        list[x%worker] +=y
    answer = max(list)
    return answer


time_table1 = [1,5,1,9]
worker1 = 3
print("solution 결과:", solution(time_table1, worker1))

time_table2 = [4,8,2,5,4,6,7]
worker2 = 4
print("solution 결과:", solution(time_table2, worker2))