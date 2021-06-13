def func_a(scores, score): #sco
    rank = 1 # 순위 #순위
    for s in scores: #전체점수를 하나씩 대입
        if s == score: #n번째 힉생의 점수와 같으면
            return rank #n번재 학생의 등수 찾기
        rank += 1 #순위 내리기
    return 0

def func_b(arr): #점수 내림차순
    arr.sort(reverse=True) #내림차순
       #리스트.sort(): 리스트 오름차순 함수
       #리스트.sort(reverse=Ture): 오름차순->내림차순

def func_c(arr, n): #n번째 학생의 점수 찾기 함수
    return arr[n] #점수목록[n] => n번째 학생의 점수

def solution(scores, n):
    score = func_c(scores, n) #n번째 학생 점수구하기
    func_b(scores)
    answer = func_a(scores, score)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores = [20, 60, 98, 59] # 학생들의 수험점수
n = 3
ret = solution(scores, n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")


