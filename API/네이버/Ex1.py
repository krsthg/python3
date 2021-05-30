#API: 미리 만들어진 코드[프로그램]
    #네이버 API

#1. 네이버 로그인
#2. 네이버에서 네이버 API 검색 => 네이버 개발자 센터 https://developers.naver.com/main/
#3. 사이트 메뉴에서 => application => 어플리케이션 등록
    #1. 어플리케이션 이름: 아무거나 넣기[파이썬입시]
    #2. 사용 API : 검색
    #3. 서비스 환경: WEB=> URL: http://python.com
#4. 사이트 메뉴 => Documents
#5. 검색결과는 딕셔너리로 호출된다. [딕셔너리 데이터 가공]
    #결과: {"item":[검색결과리스트]}
    #검색결과 리스트 중 한개당 {} 묶음

#발급받은 어플리케이션 정보를 변수에 저장
import json

id= 'VrkGrXL_lkyDHRDhegiC'
secret = 'iFQyLrQ4gd'

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import re
client_id = id
client_secret = secret
검색어 = input("블로그 검색: ")
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
#책 검색
검색어 = input("책 검색:")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8') #utf-8: 한글 지원
    json결과= json.loads(검색결과)
    #검색 결과 가공 하기
    결과리스트 = []
    for i in json결과['items']:
        t = re.sub('<.+?>','',i['title'],0,re.I|re.S)
        print(t)

else:
    print("Error Code:" + rescode)

#뉴스 검색
검색어 = input("뉴스 검색:")
encText = urllib.parse.quote(검색어)
url = "https://openapi.naver.com/v1/search/news?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
