#교차 검증을 편리하게 수행할 수 있게 해주는 cross_val_score()
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, cross_validate
import numpy as np

'''
cross_val_score(estimater, X, y=None, scoring = None, n_jobs = 1, verbose = 0, fit_params = None,
pre_dispatch = '2*n_jobs)

주요 파라미터
estimater : Classifier or Regressor를 의미
X : feature dataset
y : label dataset
scoring : 예측 성능 평가 지표
cv : 교차 검증 폴드 수
'''

iris_data = load_iris()
dt_clf = DecisionTreeClassifier(random_state=156)

data = iris_data.data
label = iris_data.target

#성능 지표는 정확도, 교차 검증 세트는 3개
scores = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=3)
print('교차 검증별 정확도 : ', np.round(scores, 4))
print('평균 검증 정확도 : ', np.round(np.mean(scores), 4))
