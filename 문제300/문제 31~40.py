#031: 34: 문자끼리는 더하기를 할 수 없고 연결된다
a="3"
b="4"
print(a+b) #문자+문자[연결된다]

#032: HiHiHi: 문자와 숫자끼리는 연산 할 수 없다. 하지만 곱[*]은 수 만큼 문자가 반복 출력
print("Hi"*3)

#033: -[하이픈]
print("-"*80)

#034
t1='python'
t2='java'
print((t1 +" "+ t2+ " ")*4) #문자끼리 +로 연결, 문자 반복 * 사용

#035: format: 형식[꾸미기]   formatiing:%
    #%s: 문자형식, %d: 정수형식
name1="김민수"
age1=10
name2="이철희"
age2=13
    #이름: 김민수 나이: 10
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

#036: format() 함수사용
    #{} 안에 들어갈 데이터 format 함수 안에 넣기
print("이름: {} 나이: {}".format(name1,age1))
print("이름: {} 나이: {}".format(name2,age2))

#037: f-string: f"문지{변수명}"
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

#038
상장주식수 = "5,969,782,550" #문자열
a = 상장주식수.replace(",","")   #교체 ,->공백
print(int(a))   #문자열->숫자열

#039
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7]) #0~6위치 문자 출력

#040 strip: 함수 사용시 앞뒤에 공백 제거 함수
data = "   삼성전자   "
print(data.strip())


