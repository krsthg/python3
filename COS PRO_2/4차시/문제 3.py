def func_a(bundle, start):
    return bundle[start::2]
    #[시작번호:끝번호:증가단위]:슬라이싱

def func_b(score1, score2): #최종 승리자 구하는 함수
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(bundle): #카드의 점수 구하기 함수
    answer = 0
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in bundle:
        answer += score_per_cards[card] #카드를 넣어서 점수를 호출하면 점수 더하기
    return answer
        
def solution(n, bundle):
    a_cards = func_a(bundle, n +1)[:n]
    b_cards = func_a(bundle, n+ 1)[:n]
    a_score = func_c(a_cards)
    b_score = func_c(b_cards)
    return func_b(a_score, b_score)

n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)
print("solution 함수의 반환 값은", ret, "입니다.")