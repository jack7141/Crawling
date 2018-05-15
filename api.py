import requests
import json
import pandas as pd
from pandas import DataFrame
def moive(URL):
    page = requests.get(URL)
    read = json.loads(page.content)#크롤링에서와 비슷한데 api를 읽어올때는 json.loads로 해서 읽어온다.
    movielist = pd.DataFrame()
    movielist = movielist.append(
        {
        '개봉일': '',
        '제목': '',
        '장르': '',
        '제작국가': '',
        '감독': ''   
        },
        ignore_index=True
    )
    get_list = len(read['movieListResult']['movieList'])
    #rint(get_list)
    for items in range(0,get_list):
        movielist.ix[items,'개봉일'] = read['movieListResult']['movieList'][items]['movieCd']#ix는 판다스에서 슬라이싱할때 쓰이는것같다~@
        movielist.ix[items,'제목'] = read['movieListResult']['movieList'][items]['movieNm']
        movielist.ix[items,'장르'] = read['movieListResult']['movieList'][items]['genreAlt']
        movielist.ix[items,'제작국가'] = read['movieListResult']['movieList'][items]['repNationNm']
        if read['movieListResult']['movieList'][items]['directors'] != []:
            movielist.ix[items,'감독'] = read['movieListResult']['movieList'][items]['directors'][0]['peopleNm']#감독이 없는경우도 생각해서 if문을 돌려주었다.
        else:
            movielist.ix[items,'peopleNm'] = ""   
    return movielist                        
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e'
print(moive(url))        
        
#print(read['movieListResult']['movieList'][0]['movieNm'])#딕셔너리 구조라서 이렇게해야함 db안에 있는 결과안에서 ㅣlist안에서 첫번째에서 이름값
#print(movielist)