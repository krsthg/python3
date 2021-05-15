    #논리: 맞는지 틀린지 판단
    #연산자:
        #산술 연산자: +더하기 -뺴기 *곱하기 /나누기 //나누기[몫] *나누기[나머지]
        #비교 연산자: >초과 <미만 >=이상 <=이하 ==같다 !==같지 않다
        #논리 연산자: and[이면서] or[이거나] ![부정]
        #대입연산자: = [오른쪽값을 왼쪽에 대입]
                 # +=[오른쪽값을 왼쪽값에 더하기한 후 왼쪽값에 대입]
                 # -=[오른쪽값을 왼쪽값에 빼기 후 왼쪽값에 대입]
                # *= /= %= 등

    #if: 논리문
        #if 논리:
        #   참[코드]
        #else:
        #   거짓[코드]
                            # if 논리:
                            #     참[코드]
                            # elif 논리2:
                            #     참2[코드2]
                            # elif 논리3:
                            #     참3[코드3]
                            # else:
                            #     거짓[코드]

                            # if 논리:
                            #     참[코드]
                            # if 논리2:
                            #     참2[코드2]
                            # if 논리3:
                            #     참3[코드3]

                            # if 논리:                    if 학년 = 3:
                            #     if 논리:                    if 성별 = 남:
                            #         참[코드]                     3학년 이면서 남학생:
                            #     else:                      else:
                            #         거짓[코드]                   3학년 이면서 여학생
                            # else:                      else:
                            #     if 논리:                    if 성별 = 남:
                            #         참[코드]                     3학년 아니면서 남학생
                            #     else:                      else:
                            #         거짓[코드]                   3학년 아니면서 여학생


#101: type(): 데이터의 타입[형태]를 확인해주는 함수
print(type(True)) #bool 타입
print(type(False)) #bool 타입
#102: False
print(3==5)

#103: True
print(3<5)

#104: True
x = 4
print(1<x<5)

#105: True
print((3==3)and(4!=3))

#106: >=
# print(3=>4)

#107: Hello World 가 출력되지 않는다
if 4<3:
    print("Hello World")

#108: Hi, there. 가 출력된다
if 4<3:
    print("Hello world")
else:
    print("Hi, there.")

#109:  1
#      2
#      4
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

#110   3
#      5
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")