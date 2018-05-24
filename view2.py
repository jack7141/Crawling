from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def keyboard(request):
    return JsonResponse(
        {
            'type': 'buttons',
            'buttons': ['소개','학교','천안볼거리','학사정보','영화정보']
        }
    )
@csrf_exempt    
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    if cafeteria_name == '소개':
        return JsonResponse({
                'message': {
                    'text':' 안녕 날 소개할께!!',
                    'text':'나는 광회봇이고, 이 프로젝트는 Python과 Django로 구현해봤어\n ',
                    'photo': {
                        'url':'http://mblogthumb2.phinf.naver.net/20110612_265/qorwjs_0_1307855937077j3a4i_JPEG/3%C3%B5%B8%B8.jpg?type=w2',
                        'width':640,
                        'height':480
                    }
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['소개','학교','천안볼거리','학사정보','영화정보']
                }
            })
    elif cafeteria_name == '학교':
        return JsonResponse({
            'message': {
                'text': '설립자 및 소개\n'+est('http://www.dankook.ac.kr/web/kor/-32'),
                'photo': {
                    'url': 'http://ph.kihoilbo.co.kr/news/photo/200912/364098_53803_3953.jpg',
                    'width': 640,
                    'height': 480

                }
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보','영화정보']
            }
        })
    elif cafeteria_name == '봄':
        return JsonResponse({
            'message': {
                'text': '<봄여행>\n'+spring('http://www.cheonan.go.kr/tour/sub02_01_01.do')
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['봄','여름','가을','겨울','처음으로']
            }
        })
    elif cafeteria_name == '여름':
        return JsonResponse({
            'message': {
                'text': '<여름여행>\n'+spring('http://www.cheonan.go.kr/tour/sub02_01_02.do')
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['봄','여름','가을','겨울','처음으로']
            }
        })
    elif cafeteria_name == '가을':
        return JsonResponse({
            'message': {
                'text': '<가을여행>\n'+spring('http://www.cheonan.go.kr/tour/sub02_01_03.do')
            },
            'keyboard': {
                'type': 'buttons',
               'buttons': ['봄','여름','가을','겨울','처음으로']
            }
        })
    elif cafeteria_name == '겨울':
        return JsonResponse({
            'message': {
                'text': '<겨울여행>\n'+spring('http://www.cheonan.go.kr/tour/sub02_01_04.do')
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['봄','여름','가을','겨울','처음으로']
            }
        })             
      
    elif cafeteria_name == '천안볼거리':
        return JsonResponse({
            'message': {
                'text': '계절을 선택해줘'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['봄','여름','가을','겨울','처음으로']
            }
        })    
    elif cafeteria_name == '처음으로':
        return JsonResponse({
            'message': {
                'text': '처음으로 돌아왔어'
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보','영화정보']
            }
        })    
    elif cafeteria_name == '영화정보':
        return JsonResponse({
            'message': {
                'text': '검색할 단어를 선택해줘'+moive('http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e')
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보','영화정보']
            }
        })                       
                               
    elif cafeteria_name == '학사정보':
        return JsonResponse({
            'message': {
                'text':  '2018학년도 축제 관련 수업진행 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656946\n'\
 +'2018학년도 축제 관련 수업진행 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656910\n'\
 +' 2018학년도 계절(하계)학기 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656619\n'\
 +' [국제]2018년 하반기 중남미 지역기구 파견인턴 선발 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=657084\n'\
 +' [국제]2019년도 일본정부(문부과학성)초청 국비 연구유학생 모집 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=657061\n'\
 +' [국제] 경기도-광동성 대학생 국제교류캠프 참가자 모집 홍보\n'
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656981\n'\
 +' [국제] 2019 불가리아 정부초청 장학생 선발 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656978\n'\
 +' [국제] 콜롬비아 정부의 스페인어 연수 프로그램 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656934\n'\
 +' [국제] 2018년도 국비유학생 선발 공고\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656931\n'\
 +' [국제] 2018년도 기술기능인 국비연수생 선발 공고\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656914\n'\
 +' 2018학년도 하계 국제영어(ICE) 수강 신청 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656913\n'\
 +' [국제] 국제계절학기 Academic Program 실시 안내(정정)\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656895\n'\
 +' 2018 하계 단국영어몰입프로그램(i EDU) 신청 안내\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656864\n'\
 +' [국제]천안캠퍼스 국제학생회(GTN) 15기 모집 안내(추가 모집)\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656844\n'\
 +' [국제] 집중외국어회화과정 Global Village 실시 안내 (강의계획서 추가)\n'\
 +'https://portal.dankook.ac.kr/web/portal/-7?p_p_id=Bbs_WAR_bbsportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=2&p_p_col_count=4&_Bbs_WAR_bbsportlet_curPage=1&_Bbs_WAR_bbsportlet_action=view_message&_Bbs_WAR_bbsportlet_messageId=656728\n'\
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['소개','학교','천안볼거리','학사정보','영화정보']
            }
        })        
    
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
        print(title, end=' \n')
        link = x.a.get('href')
        print(link)
    return crawling
            
def spring(url):
    r=requests.get(url)#소스를 가져온다
    c=r.content#소스에서 내용물을 가져온다
    soup = BeautifulSoup(c,'html.parser')#가져온 소스를 보기좋게~~해준다.
    all=soup.find('div', class_='thema_list')#필요한부분의 전체를 다 끌고온다. 주의 할것은 class는 class_로 해줘야한다.
    column = all.find_all('div',{'class':'row'})
    result = ''
    for i,items in enumerate(column):
        title=items.find('strong').text
        summary=items.find('p').text
        link = items.a.get('href')
        result += str(i+1)+". "+title + "\n" + summary+"\n" +'<자세한정보>\n'+'http://www.cheonan.go.kr'+link+"\n"
    return result   

def est(url):
    r=requests.get(url)
    c=r.content

    soup = BeautifulSoup(c,'html.parser')
    all=soup.find('div', class_='row-fluid founder')
    column = all.find_all('div',{'class':'span9'})
    result = ''
    for items in enumerate(column):
        title=items.find('div',{'class':'name bold'}).text
        summary=items.find('p').text
        result += title + "\n" + summary+"\n"
    return result           

def search(search):
    driver=webdriver.Chrome('/Program Files/chromedriver')
    driver.get('https://www.google.com')
    search=driver.find_element_by_css_selector('#lst-ib').send_keys(search)
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').send_keys(Keys.ENTER)#.click()
    time.sleep(2)    

def moive(URL):
    page = requests.get(URL)
    read = json.loads((page.content).decode('utf-8'))
    movielist = pd.DataFrame()
    movielist = movielist.append(
        {
        '개봉일': '',
        '제목': '',
        '장르': '',
        '제작국가': '',  
        },
        ignore_index=True
    )
    get_list = len(read['movieListResult']['movieList'])
    #rint(get_list)
    for items in range(1,get_list):
        movielist.ix[items,'개봉일'] = read['movieListResult']['movieList'][items]['movieCd']
        movielist.ix[items,'제목'] = read['movieListResult']['movieList'][items]['movieNm']
        movielist.ix[items,'장르'] = read['movieListResult']['movieList'][items]['genreAlt']
        movielist.ix[items,'제작국가'] = read['movieListResult']['movieList'][items]['repNationNm']
    return movielist[1:6]                            