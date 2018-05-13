import requests
from bs4 import BeautifulSoup
def est(url):
    r=requests.get(url)
    c=r.content

    soup = BeautifulSoup(c,'html.parser')
    all=soup.find('div', class_='row-fluid founder')
    column = all.find_all('div',{'class':'span9'})
    result = ''
    for i,items in enumerate(column):
        title=items.find('div',{'class':'name bold'}).text
        summary=items.find('p').text
        result += title + "\n" + summary+"\n"
    return result        
       
print(est('http://www.dankook.ac.kr/web/kor/-32'))