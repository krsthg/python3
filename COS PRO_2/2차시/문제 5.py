#문제 5
def solution(attack, recovery,hp):
    count = 0
    while (True):
        count += 1 #공격횟수 1증가
        hp -= attack #몬스터체력 -= 공격력
        if hp <= 0: #만약에 몬스터체력 <= 0 보다 작을때
            break #반복문 종료 [공격 종료]
        hp += recovery #몬스터체력
    return count

attack = 30     #캐릭터 공격력
recovery = 10   #몬스터의 회복체력
hp =60          #몬스터의 초기체력
ret = solution(attack,recovery,hp)

print("solution 함수의 결과:", ret)

#몬스터 60
#count = 1    #공격 -30 => 몬스터 30
    #회복 +10 => 몬스터 40
#count = 2        #공격 -30 => 몬스터 10
    #회복 +10 => 몬스터 20
#count = 2        #공격 -30 => 몬스터 -10[몬스터체력이 <= 0:종료]
