# #121: islower(): 소문자 인식 판단 함수
# a = input("문자 입력: ")
# if a.islower(): #소문자이면 True 아니면 False
#     print(a.upper()) #대문자로 변환
# else:
#     print(a.lower()) #소문자로 변환
#
# #122
# a = int(input("점수:"))
# if a>=81:
#     print("grade is A")
# elif a>=61:
#     print("grade is B")
# elif a>=41:
#     print("grade is C")
# elif a>=21:
#     print("grade is D")
# else:
#     print("grade is E")
#
# #123: 딕셔너리{키:값}
# a = {"달러" : 1167 , "엔" : 1.096 , "유로" : 1268 , "위안" : 171}
# b = input("금액과 통화명: ")
# 금액, 통화명 = b.split(" ") #공백 기준으로 분리
# print(금액 * a[통화명], "원") #환욜 딕셔너리에 입력한 통화명
#
# #124
# a = int(input("input number 1:"))
# b = int(input("input number 2:"))
# c = int(input("input number 3:"))
# if a>b and a>c: #a가 b보다 크면서 a가 c보다 클 때
#     print(a)
# elif b>a and b>c: #b가 a보다 크면서 b가 c보다 클 때
#     print(b)
# else:
#     print(c)
#
# print(max(a,b,c))
#
# #125
# a = input("전화번호:")
# b = a.split("-")[0] #- 기준으로 분리 후 첫번째 값 가져오기
# if  b == "011":
#     print("당신은 SKT 사용자입니다.")
# elif  b == "016":
#     print("당신은 KT 사용자입니다.")
# elif  b == "019":
#     print("당신은 LGU 사용자입니다.")
# else:
#     "알수없음"
#
# #126
# a = input("우편번호: ")
# a = a[:3] #0~2까지 가져오기[앞3자리]
# if a in ["010", "011", "012"] : #010,011,012: 강북구 번호가 포함되어 있으면
#     print("강북구")
# elif a in ["013", "014","015"]: #013,014,015: 도봉구 번호가 포함되어 있으면
#     print("도봉구")
# else:
#     print("노원구")
#
# #127
# a = input("주민등록번호: ")
# b = a.split("-")[1] #-기준으로 분리 했을때 뒷자리
# if b[0] == "1" or b[0] =="3":
#     print("남자")
# else:
#     print("여자")
#
# #128
# a = input("주민등록번호: ")
# b = a.split("-")[1]
# if 0<= int(b[1:3]) <= 8:
#     print("서울입니다")
# else:
#     print("부산입니다")
#
# #129
# a=input("주민등록번호:")
# f = int(a[0])*2 + int(a[1])*3+ int(a[2])*4 + int(a[3])*5 + int(a[4])*6+ int(a[5])*7 + int(a[7])*8+ int(a[8])*9+ int(a[9])*2+ int(a[10])*3 + int(a[11])*4 + int(a[12])*4
#         #주민번호[6]: - 제외
# s = 11-(f%11)
# t = str(s) #문자로 변환
# if a[-1] == t[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
    #해당 주소의 딕셔너리 가져오기[data] 키의 값을 가져오기
변동폭 = int(btc["max_price"])-int(btc["min_price"]) #최고가-최저가 => 차이
시가 = int(btc["opening_price"]) #시가 가격
최고가 = int(btc["max_price"])

if 시가 +변동폭>최고가:
    print("상승장")
else:
    print("하락장")