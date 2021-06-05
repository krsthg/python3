#문제 9
def soultion(characters):
    result = '' #공백
    # result += characters[0] #첫문자르 result에 저장
    for i in range(len(characters)): #하나씩 비교
        #0[첫번째] 글자 1[두번째] 비교
        if characters[i-1] != characters[i]:
            result += characters[i] #첫문자를 또 저장하면 오류

    return result

characters = 'senteeencccccceeee'
ret = soultion(characters)
print("solution 함수 결과:", ret,'.')