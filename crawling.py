import requests
from urllib.request import urlopen
import parser
from bs4 import BeautifulSoup

def crawling():
    url = 'https://portal.dankook.ac.kr/web/portal/-7'
    html = urlopen(url)
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, 'html5lib')
    table = soup.find(id="p_p_id_Bbs_WAR_bbsportlet_")
    text = table.find_all(class_="subject")

    for x in text:
        title = x.get_text()
        print(title, end=' ')
        link = x.a.get('href')
        url = 'https://portal.dankook.ac.kr/web/portal/-7' + link
        print(url)
    return crawling
print(crawling())    

