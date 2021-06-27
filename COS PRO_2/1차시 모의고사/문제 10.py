#리스트 = []
#2차원 리스트 = [[],[]]

def solution(arr, k): #arr: 2차원 리스트     #k: k번째 작은수
    answer = 0 #k번재 작은 변수
    list = [] #임시 리스트
    n = len(arr) #n: 배열의 세로길이
    for h in range(n):
        for w in range(4): #4는 배열의 가로길이
            list.append(arr[h][w])
    list.sort() #정렬 => sort: 오름차순으로 정렬
    answer = list[k-1] #인덱스는 0번부터 시작
    return answer
