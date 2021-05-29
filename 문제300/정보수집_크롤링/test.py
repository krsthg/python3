

# 현재 금 가격 크롤링

from bs4 import BeautifulSoup as bs
import urllib.request as ur

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=%ED%98%84%EC%9E%AC+%EA%B8%88+&qdt=0&ie=utf8&query=%ED%98%84%EC%9E%AC%EA%B8%88%EC%8B%9C%EC%84%B8'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')
금시세 = soup.find_all('em', {'class':'down _now_value'})

print("현재 금 시세: ", 금시세[0].text, '원 입니다.')