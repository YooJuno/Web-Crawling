'''
2025-01-16
설명)
웹 상에서 서비스 되고 있는 html 안의 내용을 파싱.
파싱한 내용을 찾아서 내 맘대로 필터 먹이고 출력

강사: 이자룡 선생님

'''

from bs4 import BeautifulSoup
import requests

# 웹 페이지 주소
url = 'https://www.devicemart.co.kr/goods/catalog?code=000200020001'

# requests를 사용해 웹 페이지 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 클래스가 'pr_list_v'인 요소 내부에서 제목 추출
pr_list_v = soup.find_all(class_='pr_list_v')  # 'pr_list_v' 클래스 검색
pr_titles = []

for item in pr_list_v:
    # 예: 내부에서 h3 태그 찾기
    title_tag = item.find('h3')  # 제목이 h3 태그에 포함되어 있다고 가정
    if title_tag:
        pr_titles.append(title_tag.get_text().strip())

# 결과 출력
for title in pr_titles:
    print('상품 이름 : ', title)
