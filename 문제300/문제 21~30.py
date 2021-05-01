#021: 안덱싱[문자순서]: 0번시작
letters='python'
print(letters[0], letters[2])

#022: 슬라이싱[시작번호: 끝번호: 단위]
    #시작번호부터 끝번호 전까지의 문자출력
license_plate = "24가 2210"
print(license_plate[4:8])
print(license_plate[-4:]) #뒤에서부터 4개

#023
string ="홀짝홀짝홀짝"
print(string[::2])
print(string[0:6:2]) #0부터 6까지 2단위로 이동[0 2 4]

#024: 슬라이싱 반대로
string = "PYTHON"
print(string[: :-1])

#025: replace("기존문자", "새로운문자") 교체함수
phone = "010-1111-2222"
p= phone.replace("-"," ")
print(p)

#026
phone = "010-1111-2222"
p= phone.replace("-","")
print(p)

#027
url = "http://sharebook.kr"
u = url.split(".")
print(u[1])

#028: 오류가 난다
# lang = 'python'
# lang[0] = 'P'
# print(lang)

#029
string = 'abcdfe2a354a32a'
s = string.replace('a','A')
print(s)

#030: aBcd
string = 'abcd'
s=string.replace('b','B')
print(s)