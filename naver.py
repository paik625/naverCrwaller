import requests

from bs4 import BeautifulSoup

# 1.어떤 웹페이지를 수집할 것이냐? URL설정


url = "https://www.naver.com/"

# 2. 해당 웹 페이지에 접속해서 데이터를 가져온다.


data = requests.get(url)

# print(data.status_code)


if (data.status_code == requests.codes.ok):

    print("성공")

    # 3.그 데이터를 원하는 형태로 파싱

    # text를 html로 파싱

    html = BeautifulSoup(data.text, 'html.parser')

    #  elm = html.select_one("selector")#단일 요소

    elms = html.select(".PM_CL_realtimeKeyword_list_base .ah_item ")

    # 리스트 형식으로 반환

    # 4.파싱한 데이터에서 원하는 자료를 찾는다.

    for elm in elms:
        a = elm.select_one('a').attrs['href']

        rank = elm.select_one('.ah_r').text

        keyword = elm.select_one('.ah_k').text

        print(rank, keyword, a)

    """
    셀럭터?

    empty tag —> 닫아주는 태그가 없음

    container tag —> 닫아주는 태그가 있음

    tag : div

    id : #NS_item

    class :  .api_item.list_item

    조합 셀렉터 :  span.api_item

    div.list span.api_item

    (div.list 안에 span.api_item이있다 ->경로를 건너뜀


    div.list > span.api_item ->중간경로를 건너뛸순없다 

    기본적으로 태그로 생각함 , .클래스 #은 아이디

    """


else:

    print("실패")
