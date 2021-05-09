    # 튜플: 리스트와 거의 유사 [] => ()
    # 단점: 튜플은 값을 바꿀수 없다
    # 튜플명 = (값1, 값2, 값3 ...)
    # 튜플명 = 값1, 값2, 값3 ...

# 071
my_variable = ()  # 튜플 생성

# 072
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 073
t1 = (1)
print(type(t1))  # int 정수 = 튜플이 아니다
t1 = (1,)
print(type(t1))  # tuple #튜플로 생성

# 074
# 튜플은 변경불가한 자료형이기 때문이다. 튜플은 값을 바꿀수가 없다.
# t1 = (1, 2, 3)
# t[0] = 'a' #0번째 순서의 값을 a로 변환

# 075: t의 타입은 tuple 이다
t = 1, 2, 3, 4

# #076
# t = ('a','b','c')
# t[0] = 'A'
#     #오류 발생: 튜플은 값을 바꿀 수 없다.

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
i = list(interest)
print(i)
# list(튜플명): 튜플을 리스트로 변환

# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
i = tuple(interest)
print(i)
# tuple(리스트명): 리스트를 튜플로 변환

# 079: apple banana cake 가 출력된다
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# 팩킹[묶음]: 리스트, 튜플, 딕셔너리
# 언패킹[묶음X]: 데이터 한개[변수]

# 080
j = tuple(range(2, 100, 2))
print(j)
# range(시작값, 끝값, 증가단위)
