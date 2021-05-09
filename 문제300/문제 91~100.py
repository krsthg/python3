#091
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}
    #딕셔너리명 = {'키':리스트, '키2':리스트2, '키3':리스트3 ...}

#092
inventory = {'메로나':[300,20],
             '비비빅':[400,3],
             '죠스바':[250,100]}
print("메로나 가격:", inventory['메로나'][0], "원") #해당하는 키의 리스트내 0번째 인덱스= => 가격

#093
print("메로나 재고:", inventory['메로나'][1], "개") #해당하는 키의 리스트내 1번째 인덱스 => 재고

#094
inventory = {'메로나':[300,20],
             '비비빅':[400,3],
             '죠스바':[250,100]}
inventory['월드콘'] = [500,7] #해당 새로운 키의 리스트를 추가
print(inventory)

#095
icecream = {'탱크보이':1200,'폴라포':1200,'빵빠레':1800,'월드콘':1500, '메로나':1000}
print(icecream.keys()) #keys() 함수 사용시 딕셔너리내 모든 키를 가져옥;

#096
print(icecream.values())

#097
print("아이스크림 금액의 총합:", sum(icecream.values()))

#098
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#099
keys = ("apple","pear","peach")
vals = (300,250,400)
result = dict(zip(keys,vals))
print(result)

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500,10300,10100,10800,11000]
close_table = dict(zip(date, close_price))
print(close_table)