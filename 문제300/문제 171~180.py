    #for 변수 in 리스트명:
    #for 변수 range(시작값, 끝값, 증가단위):

#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#172
price_list = [32100, 32150, 32000, 32500]
for i, j in enumerate(price_list):
    print(i,j)

#173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(3-i, price_list[i])

#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90+10*i, price_list[i])

#175
my_list = ["가","나","다","라"]
for i in range(0, 3):
    print(my_list[i], my_list[i+1])

print(my_list[0], my_list[1])
print(my_list[1], my_list[2])
print(my_list[2], my_list[3])

#176
my_list = ["가","나","다","라", "마"]
for i in range(2,5):
    print(my_list[i-2], my_list[i-1],my_list[i])

print(my_list[0], my_list[1],  my_list[2])
print(my_list[1], my_list[2], my_list[3])
print(my_list[2], my_list[3], my_list[4])

#177
my_list = ["가", "나", "다", "라"]
for i in range(3, 0, -1):
    print(my_list[i], my_list[i-1])

print(my_list[3],my_list[2])
print(my_list[2],my_list[1])
print(my_list[1],my_list[0])

#178: 차분값: 자신과 우측값과의 차분값
my_list = [100, 200, 400, 800]
for i in range(3):
    print(abs(my_list[i]-my_list[i+1]))

print(my_list[1]-my_list[0])
print(my_list[2]-my_list[1])
print(my_list[3]-my_list[2])

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(4):
    f = (my_list[i]+ my_list[i+1] + my_list[i +2]) /3
    print(f)

#180
low = [100, 200 , 400, 800, 1000]
high = [150, 300, 430, 880, 1000]
v = []
for i in range (0,5):
    v.append(low[i]-high[i])
