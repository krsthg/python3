def solution(shirt_size):
    answer = [0, 0,0 ,0, 0, 0]
    for i in shirt_size:
        if i == 'XS':
            answer[0] += 1
        elif i == 'S':
            answer[1] +=1
        elif i == 'M':
            answer[2] +=1
        elif i == 'L':
            answer[3] += 1
        elif i == 'XL':
            answer[4] +=1
        elif i == 'XXL':
            answer[5] +=1
    return answer

shirt_size = [ "XS",'S','L','L','XL',"S"]
print("solution 결과:", solution(shirt_size))