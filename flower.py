#붓꽃데이터 데이터를 수집할때는 A와 B가 관련있을거다 라고 정리해주어서 정리해야한다.
#pandas와 skikit을 같이 사용하면 그냥 문자열로 사용해도 출력할수있다.
import pandas as pd 
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split#결과값이 논리적으로 정답률과 가까운가를 검증하기 위해 사용한다.
csv = pd.read_csv("iris.csv")
data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label =csv["Name"]
#print(data)
#print(label)

clf=svm.SVC()
clf.fit(data,label)
results=clf.predict([
    [5.1,3.0,1.3,0.2]
])
#print(results)

#정확도검증단계
#기존의 만약 150개의 정보가 있다면 그중 100개를 기준으로 두고 나머지 50개를 100와 비교하여
#정답률이 90프로 이상이된다면 내가 만든 제품이 충분히 정확하다는것을 증명한다.

train_data, test_data, train_label, test_label=train_test_split(data, label)
clf=svm.SVC()
clf.fit(train_data,train_label)
results=clf.predict(test_data)
score = metrics.accuracy_score(results, test_label)
print("정답률 :", score)
#이후에는 csv파일에 데이터를 다 때려넣어서 기계학습을 하면된다~