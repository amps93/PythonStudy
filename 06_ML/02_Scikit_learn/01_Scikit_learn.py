# pip install scikit-learn
import sklearn
#print(sklearn.__version__)
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

'''
프로세스
1. 데이터 세트 분리 : 데이터를 학습 데이터와 테스트 데이터로 분리
2. 모델 학습 : 학습데이터를 기반으로 ML알고리즘을 적용해 모델을 학습
3. 예측 수행 : 학습된 ML 모델을 이용해 테스트 데이터의 분류를 예측
4. 평가 : 이렇게 예측된 결과값과 테스트 데이터의 실제 결과값을 비교해 ML 모델 성능을 평가 
'''

#붓꽃 데이터 세트 로딩
iris = load_iris()

#iris.data는 Iris 데이터세트에서 피처(feature)만으로 된 데이터를 numpy로 가지고 있음
iris_data = iris.data
# print(iris_data[0:3])

iris_label = iris.target
# print('iris target 값 :', iris_label)
# print('iris target 명 :', iris.target_names)

#iris 데이터 프레임으로 변환
iris_df = pd.DataFrame(iris_data, columns=iris.feature_names)
# print(iris_df.head())

#데이터셋 분류
# test_size=0.2 : 테스트데이터20% 학습데이터80%
# random_size : seed 고정
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.2, random_state=11)

#DecisionTreeClassifier 객체 생성
dt_clf = DecisionTreeClassifier(random_state=11)

#학습 수행
dt_clf.fit(X_train, y_train)

#학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(X_test)

from sklearn.metrics import accuracy_score
print('예측 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))