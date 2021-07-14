'''
estimator : classifier, regressor, pipeline이 사용될 수 있다.
param_grid : 파라미터 딕셔너리. (파라미터명과 사용될 여러 파라미터 값을 지정)
scoring : 예측 성능을 측정할 평가 방법. 보통은 사이킷런에서 제공하는 문자열 (예: ‘accuracy’)을 넣지만 별도의 함수도 직접 지정이 가능하다.
cv : 교차 검증을 위해 분할되는 폴드 수.
refit : True면 가장 최적의 하이퍼 파라미터를 찾은 뒤 입력된 estimator 객체를 해당 하이퍼 파라미터로 재학습시킨다. (default:True)
'''
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', None)

#데이터를 로딩하고 학습 데이터와 테스트 데이터 분리
iris_data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=121)
dtree = DecisionTreeClassifier()

### 파라미터를 딕셔너리 형태로 설정
parameters = {'max_depth': [1, 2, 3],
              'min_samples_split': [2, 3]
              }

#param_grid의 하이퍼 파라미터를 3개의 train, test, test set fold로 나누어 테스트 수행 결정
### refit=True가 default. True이면 가장 좋은 파라미터 설정으로 재학습 시킴
grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv=3, refit=True)

#붓꽃 학습 데이터로 param_grid의 하이퍼 파라미터를 순차적으로 학습/평가
grid_dtree.fit(X_train, y_train)

#GridSearchCV 결과를 추출해 DataFrame으로 변환
score_df = pd.DataFrame(grid_dtree.cv_results_)
# print(score_df.columns)
print(score_df[['params', 'mean_test_score', 'rank_test_score', 'split0_test_score', 'split1_test_score', 'split2_test_score']])

print('GridSearchCV 최적 파라미터 : ', grid_dtree.best_params_)
print('GridSearchCV 최고 정확도 : {0:.4f}'.format(grid_dtree.best_score_))

#GridSearchCV의 refit으로 이미 학습된 estimater 반환
estimater = grid_dtree.best_estimator_

#GridSearchCV의 best_estimater_는 이미 최적 학습이 됐으므로 별도 학습이 필요 없음
pred = estimater.predict(X_test)
print('테스트 데이터 세트 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))