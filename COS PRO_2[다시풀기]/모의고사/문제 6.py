def solution(words, word):
    answer = 0
    for i in words:
        if i[0] != word[0]:
                answer +=1
        if i[1] != word[1]:
                answer +=1
        if i[2] != word[2]:
                answer +=1
        if i[3] != word[3]:
                answer +=1
    return answer

def solution2(words, word):
    answer = 0
    for i in words:
        for x, y in zip(i, word):
            if x != y:
                answer += 1
    return answer


words = ["CODE","COED","CDEO"]
word = "CODE"
print("solution 결과:", solution(words,word))
print("solution 결과:", solution2(words,word))