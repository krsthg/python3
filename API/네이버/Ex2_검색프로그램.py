#네이버 검색 API 이용한 JSON 가공 프로그램
    #JSON: 키-값 => 한 쌍 <-딕셔너리와 유사
import urllib.request
import json
import re
#네이버 검색함수
def naver(catergory, sn):
    id= 'VrkGrXL_lkyDHRDhegiC'
    secret = 'iFQyLrQ4gd'

    #검색결과를 json으로 가져오기
    url = "https://openapi.naver.com/v1/search/" + catergory+".json"
    option = "&display="+sn+"&sort=count" #display: 출력갯수[검색결과 수]
    query = "?query="+urllib.parse.quote(input(catergory+"의 검색 정보를 입력해주세요.\nㄴ"))
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
    검색결과 = response_body.decode('utf-8')  # utf-8: 한글 지원
    json결과 = json.loads(검색결과)
    # 검색 결과 가공 하기
    결과리스트 = []
    for i in json결과['items']:
        t = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print("검색결과 =>", t)


#프로그램 코드
while True: #무한반복하기-> 0번을 입력하면 종료된다.
    print('검색[naverAPI] 프로그램')
    print('카테고리[1.뉴스 2.쇼핑 3.도서 0.종료]')
    choose = int(input("선택: ")) #입력받아 선택변수에 저장

    #선택제어
    if choose == 1:
        catergory = "news"
        sn = input("-> 뉴스를 선택했습니다.\n몇개를 출력할까요?\nㄴ")
        naver(catergory, sn)

    if choose == 2:
        catergory = "shop"
        sn = input("-> 쇼핑을 선택했습니다.\n몇개를 출력할까요?\nㄴ")
        naver(catergory, sn)

    if choose == 3:
        catergory = "book"
        sn = input("-> 책을 선택했습니다.\n몇개를 출력할까요?\nㄴ")
        naver(catergory, sn)

    if choose == 0:
        print("-> 이용해주셔서 감사합니다 :)")
        break #반복문 종료: while 문 탈출