#041: upper() 함수: 대문자로 변환해주는 함수
ticker = "btc_lrw"
print(ticker.upper())

#042: lower() 함수: 소문자로 변환해주는 함수
ticker = "RTC_LRW"
print(ticker.lower())

#043: capitalize() 함수: 첫글자를 대문자로 변환해주는 함수
h = "hello"
print(h.capitalize())

#044: endswith() 함수: 끝나는 문자가 맞는지 확인 함수
file_name = "보고서.xlsx" #엑셀파일
print(file_name.endswith("xlsx")) #파일에사 "xlsx" 로 끝나는지 확인
        #맞으면 Ture, 아니면 False

#045: 문자열이 'xlsx' 또는 'xls' 로 끝나는지 확인하는 함수
file_name = "보고서.xlsx"
print(file_name.endswith(('xlsx','xls')))
        #xlsx혹은 xls로 끝나는지 확인

#046: startswith() 함수: 시작하는 문자가 맞는지 확인하는 함수
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

#047
a = "hello world"
b = a.split(" ")
print(b) #공백 기준으러 분리되어 리스트에 저장

#048: _[언더바] -[하이픈]
a = "btc_krw"
b = a.split("_")
print(b) #_[언더바] 기준으로 분리되어 리스트에 저장

#049
date = "2020-05-01"
b = date.split("-")
print("연도: "+ b[0], "월: " +b[1], "일: "+b[2] )

#050: strip(): 양쪽 공백 제거 #rstrip(): 오른쪽 공백 제거
date = "039490     "
print(date.rstrip())
