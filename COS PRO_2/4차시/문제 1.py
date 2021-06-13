def solution(schedule): #상담을 받지 못한 [x] 학생수 찾는 함수
    answer = [] #상담을 받지 못한 학생 리스트
    for idx, i in enumerate(schedule):
        #idx: 리스트내 요소 수
        #i: 리스트내 요소 값
        #for 인덱스 번호, 값 enumerate(리스트)
            #값이 X 이면 answer(결과) 리스트에 요소번호를 저장
        if i == "X": #i가 X이면 상담을 못받음
            answer.append(idx+1) #X를 받은 학생의 번호 저장
    return answer

schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)


print("solution 함수의 반환 값은", ret, "입니다.")