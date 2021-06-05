#문제 4
import math

def solution(words):
    answer = ''
    for i in words:
        if len(i)>= 5:   #문자길이가 5글자 이상이면
            answer += i  #문자1+=문자2 => 문자1문자2 연결
    if len(answer)<1: #결과가 1보다 작으면
        answer = 'empty'
    return answer

        #my, is를 제이한 5글자 이상 단어들끼리 이어붙이기
words1 = ["my",'favorite','color','is','violet']
ret1=solution(words1)

print("solution 함수의 결과:",ret1)

words2 = ['yes','i','am']
ret2 = solution(words2)

print("solution 함수의 결과:",ret2)
