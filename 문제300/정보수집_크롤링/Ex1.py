#정보수집_크롤링 패키지
    #1. Ex1.py

#크롤링: 인터넷에서 데이터 추출하기

#1. BeautifulSoup 설치
from bs4 import BeautifulSoup as bs #html 읽는 메소드 제공 => read()
import urllib.request as ur #파이썬 html 가져오기 => urlopen

# 1. 인터넷 주소 넣기
url = 'http://quotes.toscrape.com/'

#2. 해당(url) 인터넷을 파이썬에서 열기해서 html 변수에 저장
html = ur.urlopen(url)

#3. read(): 인터넷 읽어오기
soup = bs(html.read(), 'html.parser')

# 4. 읽어온 파일중 찾기 ('span') 찾아서 첫번재 텍스트 가져오기
print(soup.find_all('span')[0].text)

#find_all(): 찾는 값 모두 가져오기
print(soup.find_all('span')[2].text)
print(soup.find_all('span')[4].text)

#모든 span 출력
for i in soup.find_all('span'):
    print(i.text)

#span에 포함된 해당 클래스만 찾기
for i in soup.find_all('span', {"class":"quote"}):
    print(i.text)