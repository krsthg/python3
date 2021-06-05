#문제 1

max_product_number = 10

def func_a(gloves):
    #각 제품별 0으로 설정
    #각 제품별 개수를 0으로 설정해서 리스트 만들기
    counter = [0 for _ in range(max_product_number+1)]
    for x in gloves: #해당 장갑의 제품번호 = 인덱스 번호
        counter[x] += 1
    return counter
        #순서도 = [2,1,2,2,4]
        #왼손 count [1,3,0,1,0,0,0,0,0,0]
        #오른손 count = [1,2,0,2,0,0,1,0,0,0]

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)  #왼손 장갑 제품별 갯수 세기
    right_counter = func_a(right_gloves)  #오른손 장갑 제품별 갯수 세기

    total = 0 #각 제품 번호별 최대한 많은 장갑 쌍 개수 세기
    for i in range(1, max_product_number+1):
        total += min(left_counter[i], right_counter[i])
    return  total

left_gloves = [2,1,2,2,4]   #왼쪽장갑의 제품번호
right_gloves = [1,2,2,4,4,7] #오른쪽장갑의 제품번호
ret = solution(left_gloves,right_gloves)

print("solution 함수의 결과:",ret, '.')
