def solution(scores):
    grade_counter = [0 for i in range(5)]
    #grade_counter: 학점목록에 학점 5개를 0으로 설정

    for x in scores:
        if 85<=x<=100: #x가 85점 이상이면
            grade_counter[0] += 1 #학점목록[0] = A 학점 한명 추가
        elif 70<=x<=84: #x가 70점 이상이면
            grade_counter[1] += 1 #학점목록[1] = B 학점 한명 추가
        elif 55<=x<=69: #x가 55점 이상이면
            grade_counter[2] += 1 #학점목록[2] = C 학점 한명 추가
        elif 40<=x<=54: #x가 40점 이상이면
            grade_counter[3] += 1 #학점목록[3] = D 학점 한명 추가
        else:
            grade_counter[4] += 1 #학점목록[4] = F 학점 한명 추가
    return grade_counter