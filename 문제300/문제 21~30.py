#021
letters='python'
print(letters[0], letters[2])

#022
license_plate = "24가 2210"
print(license_plate[4:8])

#023
string ="홀짝홀짝홀짝"
print(string[::2])

#024
string = "PYTHON"
print(string[: :-1])

#025
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