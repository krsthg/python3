#변수는 저장 공간
    #num = 10
#리스트는 여러개의 변수를 저장하는 공간
    #list = [변수1, 변수2, 변수3 ...]

#051: 여러개 변수를 저장하는 공간 [] 안에 변수 넣기
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

#052: 리스트명.append(추가할변수): 리스트에 변수 추가
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

#053: 리스트명.insert(인덱스 번호, 추가할 변수): 인덱스 번호에 변수 추가
movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "배트맨"]
movie_rank.insert(1, "슈퍼맨") #1번 인덱스에 슈퍼맨 추가
print(movie_rank)

#054: del 리스트명[인덱스번호]: 해당 인덱스번호가 삭제
movie_rank = ["닥터 스트레인지","슈퍼맨", "스플릿", "럭키", "배트맨"]
del movie_rank[3]
print(movie_rank) #럭키 삭제

#055
movie_rank = ["닥터 스트레인지", "슈퍼맨","스플릿", "배트맨"]
del movie_rank[2] # => 스플릿 삭제 => 배트맨 => 스플릿 자리로 이동
del movie_rank[2] # => 배트맨 삭제
print(movie_rank)

#056: 리스트 합치기: 리스트명 + 리스트명
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python","Go", "C#"]
langs = lang1 + lang2
print(langs)

#057: 최대값[max()], 최솟값[min()]
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

#058: 합계[sum()]
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059: 계수[len()]
cook = ["피자", "김밥", "만두" , "양념치킨" , "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면","팥빙수","김치전"]
print(len(cook))

#060: 합계/계수 = 평균    sum/len = 평균
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))