def solution(price, money): #price: 구매한 가격들의 리스트    #money: 지불한 금액
    # answer = 0
    # price2= 0
    # for i in price:
    #     price2 += i
    # if price2>money:
    #     return -1
    # else:
    #     answer= money- price2
    # return answer
    answer = money -sum(price) #거스름돈 구하기
                    #sum(리스트): 리스트내 요소들의 전체 합계
    if answer <0: #만약 지불한 금액보다 구매할 총 구매금액이 더 크면
        answer = -1 #만약 거스름돈이 마이너스이면 -1 리턴
    return answer