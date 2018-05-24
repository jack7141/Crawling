import requests
from bs4 import BeautifulSoup
def spring(url):
    r=requests.get(url)#소스를 가져온다
    c=r.content#소스에서 내용물을 가져온다
    #decode = c.decode('utf-8')#한글을 읽게해주고 소스도 까아알꼼하게 나오게 해준당~
    soup = BeautifulSoup(c,'html.parser')#가져온 소스를 보기좋게~~해준다.
    all=soup.find('div', class_='thema_list')#필요한부분의 전체를 다 끌고온다. 주의 할것은 class는 class_로 해줘야한다.
    column = all.find_all('div',{'class':'row'})
    result = ''
    for i,items in enumerate(column):
        title=items.find('strong').text
        summary=items.find('p').text
        link = items.a.get('href')
        result += str(i+1)+". "+title + "\n" + summary+"\n" +'<자세한정보>\n'+'http://www.cheonan.go.kr'+link+"\n"
    #return result        
       


url ='http://www.cheonan.go.kr/tour/sub02_01_02.do'
print(spring(url))
        
            
    