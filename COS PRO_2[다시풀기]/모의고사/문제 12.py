def solution(cards):
    answer = [0,0,0]
    answer = [0,0,0]
    j = 0
    for i in cards:
        if i[0] == "blue":
            answer[0] +=1
        elif i[0] == "black":
            answer[1] +=1
        elif i[0] == "red":
            answer[2] += 1
        j += int(i[1])
    if answer[0] == 3 or answer [1] == 3 or answer[2] == 3:
        j *=3
    elif answer[0] == 2 or answer [1] == 2 or answer[2] == 2:
        j *= 2
    return j

cards1 = [["blue","2"],["red","5"], ["black","3"]]
cards2 = [["blue","5"],["blue","2"], ["black","3"]]
print("solution 결과:", solution(cards1))
print("solution 결과:", solution(cards2))