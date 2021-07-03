#You may use import as below.
#import math

def solution(shirt_size):
    #Write code here.
    answer = [0, 0, 0, 0, 0, 0]
    for ss in shirt_size:
        if ss == "XS":
            answer[0] +=1
        if ss == "S":
            answer[1] +=1
        if ss == "M":
            answer[2] +=1
        if ss == "L":
            answer[3] +=1
        if ss == "XL":
            answer[4] +=1
        if ss == "XXL":
            answer[5] += 1

    return answer

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")