#문제 5
def solution(attack, recovery,hp):
    count = 0
    while (True):
        count += 1
        hp -= 1
        if hp <= 1:
            count += 1
        hp += 1
    return count

attack = 30
recovery = 10
hp =60
ret = solution(attack,recovery,hp)

print("solution 함수의 결과:", ret)