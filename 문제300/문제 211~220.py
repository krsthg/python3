#211
#안녕 Hi

#212
#7, 15

#213
#함수에 인수가 없기 때문이다

#214
#문자와 정주는 더할 수 없기 때문이다.

#215
def print_with_smile():
    a = input()
    print(a+ " :D")

#216
print_with_smile()

#217
def print_upper_price():
    a = int(input())
    print(a*1.3)

#218
def print_sum():
    a = int(input())
    b= int(input())
    print(a+b)

#219
def print_arithmetic_operation():
    a = int(input())
    b= int(input())
    print(a,"+", b,"=",a+b)
    print(a,"-", b,"=", a-b)
    print(a,"*",b, "=", a*b)
    print(a, "/", b, "=", a/b)

#220
def print_max():
    a= int(input())
    b = int(input())
    c = int(input())
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)