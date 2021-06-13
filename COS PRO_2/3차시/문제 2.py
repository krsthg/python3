def func_a(current_grade, last_grade, rank, max_diff_grade): #장학생 수 구하기
    arr_length = len(current_grade) #전체 학생수
    count = 0 #장학생 수
    for i in range(arr_length): #전체 학생수 만큼 반복
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:  # 80점 이상, 상위 10%
            count += 1 #장학생 수 증가
        elif current_grade[i] >= 80 and rank[i] == 1: #80점 이상, 석차 1등
            count += 1 #장학생 수 증가
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]: #이번학기-전 학기 성적이 func_b와 같고 양수
            count += 1
    return count

def func_b(current_grade): #석차 구하는 함수
    arr_length = len(current_grade) #len(리스트):리스트 내 요소 개수 구하는 함수
    rank = [1] * arr_length
    for i in range(arr_length): #학생수 만큼 반복
        for j in range(arr_length): #학생수 만큼 반복
            if current_grade[i] < current_grade[j]: #이번학기[i]<저번학기[j]
                rank[i] += 1
    return rank #더 작으면 순위 내리기

    #i=0, j=0   j=1    j=2     j=3     j=4    j=5
    #i 1증가 할때마다 j는 5번 실행

def func_c(current_grade, last_grade): #최댓값 구하기[가장 성적이 많이 오른 학생]
    max_diff_grade = 1
    for i in range(len(current_grade)):
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
        #max(현재최댓값,(이번학기-직전학기))
    return max_diff_grade

def solution(current_grade, last_grade):
    rank = func_b(current_grade)
    max_diff_grade = func_c(current_grade,last_grade)
    answer = func_a(current_grade,last_grade,rank,max_diff_grade)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95]
last_grade = [35, 65, 80, 50, 20, 60]
ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")