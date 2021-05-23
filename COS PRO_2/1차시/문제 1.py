#문제 1: 리스트에 저장된 문자열의 갯수를 다시 리스트에 담기
def solution(shirt_size): #함수 만들기
    size_count = [0, 0, 0, 0, 0, 0] #1. 티셔츠 사이즈별 개수를 담을 리스트 선언
                # XS, S, M, L, XL, XXL
    for ss in shirt_size: #리스트 반복 => 리스트내 항목이 변수에 하나씩 대입
        if ss == "XS":              #2. 만약에 XS이면 첫번째 인덱스 +1
            size_count[0] += 1
        if ss == "S":               #2. 만약에 S이면 첫번째 인덱스 +1
            size_count[1] += 1
        if ss == "M":               #2. 만약에 M이면 첫번째 인덱스 +1
            size_count[2] += 1
        if ss == "L":               #2. 만약에 L이면 첫번째 인덱스 +1
            size_count[3] += 1
        if ss == "XL":              #2. 만약에 XL이면 첫번째 인덱스 +1
            size_count[4] += 1
        if ss == "XXL":             #2. 만약에 XXL이면 첫번째 인덱스 +1
            size_count[5] += 1
    return size_count #함수가 끝나면서 돌려주는 값 => return => 리스트를 리턴

shirt_size = ["XS","S","L","L","XL","S"] #학생들이 원하는 사이즈 리스트
ret = solution(shirt_size) #함수 불러내기

print("solution: return value of the function is",ret," .")
