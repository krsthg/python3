
#차이와 사용방법
    #변수:
    #리스트:
    #튜플:
    #딕셔너리:

#061
price = ["'20180728'", 100, 130, 140, 150, 160, 170]
print(price[1:])
    #[인덱싱] = [1:] = 2번째값부터 끝까지

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[ : : 2])
    #[인덱싱] = [::2] = 0번째부터 끝까지 2개씩 이동 = 0 2 4 6 8
    #[시작번호:끝번호:이동단위]

#063
print(nums[1::2])
    #[슬라이싱] = [1::2] = 1번째 값부터 끝까지 2개씩 이동 = 1 3 5 7 9

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
    #[슬라이싱] = [::-1] = 역방향

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
    #join 함수: 리스트 내 항목을 어떠한 문자를 기준으로 합칠때 사용하는 함수

#067
print("/".join(interest))

#068
print("\n".join(interest))
    #\n: 줄바꿈 제어문자       \t:들여쓰기 제어문자

#069
string = "삼성전자/LG전자/Naver"
interest=string.split('/')
print(interest)

#070
date = [2, 4, 3, 1, 5, 10 ,9]
date.sort()
print(date)
    #sort: 내림차순     reverse: 오름차순
date.sort(reverse=True)
print(date)