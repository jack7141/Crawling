#방식 Get,Post,del,Put
#대상:https://search.naver.com/
#추가적인 정보
#-경로 :search.naver
#-데이터:?where=nexearch(=요청매개변수라고도 함! )
# &sm=top_hty
# &fbm=1&ie=utf8
# &query=%EC%B4%88%EC%BD%9C%EB%A6%BF(=초콜릿이란 뜻인데 아시다시피 웹은 양키들꺼니깐...영어로 
# 표현하려고한것 그래서 EnCoding즉 지금 %b%a이런게 인코딩된상태고 반대가 디코딩, Decoding이 필요함)
#    r=requests.get(url)#소스를 가져온다
#     c=r.content#소스에서 내용물을 가져온다
import requests
import urllib.parse
URL= 'https://search.naver.com/'
values = {
    'where' : 'nexearch',
    'sm' : 'top_hty',
    'fbm' : '1',
    'ie' : 'utf-8',
    'query' : '초콜릿'
}
params = urllib.parse.urlencode(values)#인코딩작업!
Target = URL+'?'+params#위의 벨류를 설정해 줘서 자동으로 다음 벨류가 되면 &로 나눠진다.
print(Target)
#b' 바이럴??
data = requests.get(Target)
read = data.content
decode = read.decode('utf-8')#euc-kr 개발할때 잘안되는 경우가 있으므로 디코드를 하고 확인하고 넘어가는편이 현명하다
print(decode)