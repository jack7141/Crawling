import requests
import urllib.request
from bs4 import BeautifulSoup
import time
#column = all.find_all('div',{'class':'span9'})
URL = 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105'
response = requests.get(URL)
read = response.content
soup = BeautifulSoup(read, "html.parser")
results = soup.select('.classfy a')
#all=soup.find('div', {'class':'cluster_text'})이런 방법도 있고 아래와 같은 방법도 있다. 이건 뭔가 하나만 딱 잡아내게해준다? 하튼 기능은 똑같으나 아래것이 더 직관적이다.
for item in results:
    print('제목 :',item.attrs['title'])
    url_article = item.attrs['href']
    response = requests.get(url_article)
    read = response.content
    soup_article = BeautifulSoup(read, "html.parser")
    content = soup_article.select_one('#articleBodyContents')
    #print(content.contents)
    output = ""
    for result in content.contents:#가공하기 위해서 한번더 돌려준다.
        stripped = str(result).strip()
        if stripped == "":continue
        if stripped[0] not in ["<", "/"]:
            output += str(result).strip()#공백을 삭제해줌 
            final = output.replace("본문 내용TV플레이어","")
    print(final)
    time.sleep(1)
