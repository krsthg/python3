#2차원 리스트: [[1차원],[1차원],[1차원]]
    #행: 가로
    #열: 세로
    #딕셔너리: 키외 값으로 이루어진 한 쌍 => 여러개 저장하는 공간{}

#181
apart = [["101호","102호"],["201호","202호"],["301호","302호"]]

#182
stock = [["시가",100,200,300] ,["종가",80,210,330]]

#183
stock = {"시가":[100,200,300], "종가":[80,210,330]}

#184
stock = {"10/10":[80,110,70,90],"10/11":[210,230,190,200]}

#185
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j, "호")

#186
apart = [[101,102],[201,202],[301,302]]
for i in apart[:: -1]:
    for j in i:
        print(j , "호")

#187
apart = [[101, 102],[201,202],[301,302]]
for i in apart[::-1]:
    for j in i [::-1]:
        print(j,"호")

#188
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j, "호")
        print("-----")

#189
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j, "호")
    print("-----")

#190
apart = [[101,102],[201,202],[301,302]]
for i in apart:
    for j in i:
        print(j, "호")
print("-----")