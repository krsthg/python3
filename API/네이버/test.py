import urllib.request
import json
import re
def naver(catergory, sn):
    id= 'VrkGrXL_lkyDHRDhegiC'
    secret = 'iFQyLrQ4gd'

    url = "https://openapi.naver.com/v1/search/" + catergory+".json"
    option = "&display="+sn+"&sort=count"
    query = "?query="+urllib.parse.quote(input(catergory2+"의 검색 정보를 입력해주세요.\nㄴ"))
    url_query = url +query +option

    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",id)
    request.add_header("X-Naver-Client-Secret", secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)
    검색결과 = response_body.decode('utf-8')
    json결과 = json.loads(검색결과)
    결과리스트 = []

    for i in json결과['items']:
        t = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print("검색결과 =>", t)

        if catergory == 'movie':
            print('-> 영화제목:',re.sub('<.+?>', '', i['title'], 0, re.I | re.S))
            print('-> 감독:', re.sub('<.+?>', '', i['director'], 0, re.I | re.S))
            print('-> 출연배우:', re.sub('<.+?>', '', i['actor'], 0, re.I | re.S))
            print('-> 평점:', re.sub('<.+?>', '', i['userRating'], 0, re.I | re.S))

        if catergory == 'shop':
            print('-> 상품명:', re.sub('<.+?>', '', i['title'], 0, re.I | re.S))
            print('-> 제조사명:', re.sub('<.+?>', '', i['maker'], 0, re.I | re.S))
            print('-> 브랜드명:', re.sub('<.+?>', '', i['brand'], 0, re.I | re.S))

        if catergory == 'book':
            print('-> 책제목:', re.sub('<.+?>', '', i['title'], 0, re.I | re.S))
            print('-> 저자명:', re.sub('<.+?>', '', i['author'], 0, re.I | re.S))
            print('-> 출판사명:', re.sub('<.+?>', '', i['publisher'], 0, re.I | re.S))

#프로그램 코드
while True:
    print('검색[naverAPI] 프로그램')
    print('카테고리[ 1.쇼핑 2.도서 3.영화  0.종료]')
    choose = int(input("선택: "))

    if choose == 1:
        catergory = "shop"
        catergory2 = '쇼핑'
        sn = input("-> 쇼핑을 선택했습니다.\n몇개를 출력할까요?\nㄴ")
        naver(catergory, sn)

    if choose == 2 :
        catergory = "book"
        catergory2 = '도서'
        sn = input("-> 도서를 선택했습니다.\n몇개를 출력할까요?\nㄴ")
        naver(catergory, sn)

    if choose == 3:
        catergory = "movie"
        catergory2 = '영화'
        sn = input("-> 영화를 선택했습니다.\n몇개를 출력할까요?\nㄴ")
        naver(catergory, sn)

    if choose == 0:
        print("이용해주셔서 감사합니다 :)")
        break
