def solution(classes, m):
    answer = 0
    for students in classes: #교실별 학생수 하나씩 대입
        answer += students// m #학생수 // 답당 학생수       80//30 => 2
        if students % m != 0: #나머지가 있으묜
            answer += 1 #조교 한명 추가
    return answer

classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)
print("solution 함수의 반환 값은", ret, "입니다.")