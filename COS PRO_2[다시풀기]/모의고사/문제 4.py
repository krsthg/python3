def solution(words):
    answer = ''
    for i in words:
        if len(i) >= 5:
            answer += i
    if len(answer)<1:
        answer = 'empty'
    return answer

words1 = ["my", "favorite", "color", "is", "violet"]
print("solution 결과:", solution(words1))

words2 = ["yes", "i", "am"]
print("solution 결과:", solution(words2))