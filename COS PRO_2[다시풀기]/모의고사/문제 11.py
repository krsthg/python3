def solution(people):
    answer =[0,0,0,0]
    for i in people:
        if i<95:
            answer[0]+=1
        elif 100>i>=95:
            answer[1]+=1
        elif 105> i >=100:
            answer[2] +=1
        elif 105<= i:
            answer[3] +=1
    return answer

people = [97, 102, 93, 100, 107]
print("solution 결과:", solution(people))