import math

def solution(words, word): #단어목록 만큼 하나씩 반복
    count = 0
    for comp in words: #검사 단어 = x, 단ㅇ
        for x,y in zip(comp, word):
            if x != y:
                count +=1
    return count


words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)

print("solution 함수의 반환 값은", ret, "입니다.")