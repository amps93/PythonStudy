from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#테스트 데이터를 활용하지 않고 학습 데이터 세트로만 학습 후 예측
iris = load_iris()
dt_clf = DecisionTreeClassifier()
train_data = iris.data
train_label = iris.target
dt_clf.fit(train_data, train_label)

#학습 데이터 세트로 예측 수행
pred = dt_clf.predict(train_data)
print('예측 정확도 : ', accuracy_score(train_label, pred)) #정확도 1.0 / 이미 답을 알고 있기 때문

#train_test_split() 사용
iris_data = load_iris()
dt_clf = DecisionTreeClassifier()

#테스트 30%, 학습 70%
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.3, random_state=121)

#모델 이용해 정확도 측정
dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
print('예측 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))