def solution(stones): #stoneㄴ: 징검다리에 적혀있는 두
    cnt = 0 #점프한 개수
    current = 0 #현재 개구리의 위치
    n = len(stones) #현재위치가 징검다르 개수면
    while current <n: #현재위치가 마지막징검다리 까지 반복
        current += stones[current] #개구리 현재위치에 더해주기[징검다리에 적혀있는 수로]
        cnt += 1 #점프수 증가
    return cnt #점프수 반환