#naver.com/robots.txt=>해당페이지에서 크롤링하지 말아라하는 사항이 나와있음 하면 불법임...ㅠ
#pip3 install -U scikit-learn scipy matplotlib scikit-image 이것들을 설치해 주었음
from sklearn import svm,metrics#메트릭스는 정답률을 쉽게 구해주는 매소드

clf = svm.SVC()#SVC알고리즘이 아래 fit함수를 학습히게된다.
#clf.fit(데이터,답)
clf.fit([
    [0,0],#벡터라고함
    [1,0],                      #데이터를 던져주고
    [0,1],
    [1,1]
]
,[
    0,
    1,                          #답을 던져줘서
    1,
    0
])
results =clf.predict([#우리가 원하는 것의 값을 넣어서 답을 구한다
    [0,0],                      #결과를 예측한다..
    [1,0]
])
print(results)
#정답률을 구해보자~
datas =[[0,0],[1,0],[0,1],[1,1]]
labels = [0,1,1,0]
examples = [[0,0],[1,0]]
examples_label = [0,1]#정답을 구한것을 보여준다.
score = metrics.accuracy_score(examples_label, results)
print("정답률 :" ,score)