def solution(s):
    s_lst = list(s) #list(s):
    n = len(s)
    for i in range(n):
        if s_lst[i] == 'a': #만약 리스트에[i]=='a' 이면
            s_lst[i] = 'z' #z로 변경
        #if s_lst[i] == 'z':
        elif s_lst[i] == 'z': #만약 리스트에[i]=='z' 이면
            s_lst[i] =  'a' #a로 변경
    return "".join(s_lst)

#첫번째 if가 T가 아니더라도 두번째 if도 검사
#if 조건1:
#if 조건2:

#첫번째 if가 T이면 두번째 elif는 검사 안함
#if 조건1:
#elif 조건2:
