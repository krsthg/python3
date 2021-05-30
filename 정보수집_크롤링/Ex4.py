#자동차 모델명을 입력받아 출시가 크롤링
from bs4 import BeautifulSoup as bs #html 언어 읽어주는 함수 제공
import urllib.request as ur
import urllib

while True:#무한 입력받기
    모델명 = input("모델명:")
    검색어 = urllib.parse.quote(모델명)
    주소 = 'https://search.naver.com/search.naver??ie=utf8&query='+검색어

    웹문서 = ur.urlopen(주소)
    soup = bs(웹문서.read(),'html.parser')
    출시가 = soup.find_all('span',{'class':''})
    찾는문자 = "판매" #판매가격 찾기
    for i in 출시가:
        j= 찾는문자 in i.text #만약에 가격에 판매가가 포함되어 있으면
        if j: #출력
            print("출시가:", i.text)
            #아니면 출력 X