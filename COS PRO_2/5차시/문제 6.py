def solution(korean, english):
    answer = 0
    #math = 210 - korean + english => 오답
    math = 210 - (korean + english) #수학 = 전체점수 -(국어+영어)
    if math > 100: #만약 수학점수가 100보다 크면
        answer = -1 #-1[비정상]
    else: #아니면
        answer = math #수학점수 반환
    return answer

korean = 70 #국어점수
english = 60 #영어점수
ret = solution(korean, english)
print("solution 함수의 반환 값은", ret, "입니다.")