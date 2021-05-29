#신촌 날씨 온도 출력하기

from bs4 import BeautifulSoup as bs #html 언어 읽어주는 함수 제공
import urllib.request as ur
import urllib

지역 = input("지역:")
검색어 = ur.parse.quote(지역+'날씨')

주소 = 'https://search.naver.com/search.naver??ie=utf8&query=' +검색어

주소 = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A0%EC%B4%8C%EB%82%A0%EC%94%A8&oquery=%EB%B6%84%EB%85%B8%EC%9D%98+%EC%A7%88%EC%A3%BC%3A+%EB%8D%94+%EC%96%BC%ED%8B%B0%EB%A9%94%EC%9D%B4%ED%8A%B8&tqi=h7ciXlp0JXVss4YZT90ssssstYs-188231'
웹문서 = ur.urlopen(주소)
soup = bs(웹문서.read(),'html.parser')

온도 = soup.find_all('span', {"class":"todaytemp"})
print("현재 신촌 날씨:", 온도[0].text,"도 입니다.")

#신촌 미세먼지 출력하기
미세먼지 = soup.find_all('dd',{"class":"lv1"})
print("현재 신촌 미세먼지:",미세먼지[0].text)

#신촌 오존지수 출려하기
오존지수 = soup.find_all("dd",{"class":'lv2'})
print("현재 신촌 오존지수:", 오존지수[0].text)