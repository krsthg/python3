def solution(ladders, win):
    answer = 0
    player = [1, 2, 3, 4, 5, 6] #플레이어 수
    for e in ladders: #가로 사다리[플레이어 위치 교환]
        #교환[swap]: 2개의 변수르 교환하는 방법
        temp = player[e[0]-1] #첫번재 사다리 temp 저장
        player[e[0]-1] = player[e[1]-1] #두번째 사다리를 첫번재 사다리에 저장
        player[e[1]-1] = temp #temp를 두번째 사다리에 저장
    answer = player[win-1]
    return answer

ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]] #가로 사다리
win = 3
ret = solution(ladders, win)
print("solution 함수의 반환 값은", ret, "입니다.")