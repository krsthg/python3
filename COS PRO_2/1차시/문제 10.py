#문제 10: 평균보다 작은 수가 몇개인지 출력하는 함수

def soultion(data):
    total = sum(data)   #총점수
    # average = len(data)/total #총점수/갯수
    average = total/len(data) #갯수/총점수
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return  cnt

data1=[1,2,3,4,5,6,7,8,9,10]
ret1 = soultion(data1)
print('solution 함수 결과',ret1,'.')

data2=[1,1,1,1,1,1,1,1,1,10]
ret2 = soultion(data2)
print('solution 함수 결과',ret2,'.')