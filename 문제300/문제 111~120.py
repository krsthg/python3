#111: input(): 키보드로 문자를 입력받는 함수
print("안녕하세요"*2)

#112
a = int(input("숫자를 입력하세요: "))
print(a+10)

#113
a = int(input("짝수, 홀수 판별:"))
if a%2==0:
    print("짝수")
else:
    print("홀수")

#114
a = int(input("숫자를 입력하세요: "))
if a + 20<225:
    print(a+20)
else:
    print(225)

#115
a = int(input("숫자를 입력하세요: "))
if 0<a-20<255:
    print(a-20)
elif 0>a-20:
    print(0)
else:
    print(255)

#116
a = input("현재 시간: ")
if a[3:] == "00":
    print("현재 정각 입니다")
else:
    print("현재 정각이 아닙니다")

#117
fruit = ["사과","포도","홍시"]
a = input("좋아하는 과일: ")
if a in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#118
warn_investment_list = ["Microsoft","Google","Naver","Kakao","SAMSUNG","LG"]
a= input("종목명: ")
if a in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

#119
fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
a = input("좋아하는 계절: ")
if a in fruit:
    print("정답입니다")
else:
    print("오답입니다")

#120
fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
a= input(">>제가 좋아하는 과일은: ")
if a in fruit.values() :
    print("정답입니다.")
else:
    print("오답입니다.")
