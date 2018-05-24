import requests
from bs4 import BeautifulSoup
# session.get(url)
# session.post(url)
# session.put(url)
# session.delete(url)
#로그인
data = {
    "return_url":"aaaaa",
    "m_id": "id",
    "m_passwd":"asdfasdf",
}#http://google.com?a=10&b=20이런식으로 들어간다.
session =requests.session()
res = session.get('http://google.com', data=data)
res.raise_for_status()#요청을 걸어주는 함수
url = 'asdf'
res = session.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
text = soup.select(".clacc hawe").get_text()
print(res.text)
