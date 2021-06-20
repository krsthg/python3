#import math

def solution(cards):
    answer = 0
    #카드의 색상 수 세기
    cardcolor = [0 for _ in range(3)] #0을 3개 가지고 있는 리스트
    for card in cards:
        if card[0] == "black":
            cardcolor[0] +=1
        elif card[0] == "blue":
            cardcolor[1] +=1
        elif card[0] == "red":
            cardcolor[2] +=1
        answer += int(card[1]) #카드 숫자를 answer 에 누적해서 더하기
    if cardcolor[0] == 3 or cardcolor[1] == 3 or cardcolor[2] == 3:
        answer *=3 #동일한 카드가 3개이면 총합에 *3
    elif cardcolor[0] == 2 or cardcolor[1] == 2 or cardcolor[2] == 2:
        answer*=2 #동일한 카드가 2개이면 총합에 *2
    return answer

cards1 = [["blue", "2"], ["red", "5"], ["black", "3"]]
ret1 = solution(cards1)
print("solution 함수의 반환 값은", ret1, "입니다.")

cards2 = [["blue", "2"], ["blue", "5"], ["black", "3"]]
ret2 = solution(cards2)
print("solution 함수의 반환 값은", ret2, "입니다.")