#
# (1) 회귀모형 평가
#   - 구축한 회귀모형에 대한 평가 지표로 결정 계수와 수정된 결정 계수 이외에도 RMSE, MSE 등을 이용할 있다. 
#
#   1) MSE(Mean Squared Error, 평균 제곱 오차)
#      + MSE 값이 낮을수록 정확도가 높다.
#      ==> mse(actual, predicted)
#
#   2) RMSE(Root Mean Squared Error, 평균 제곱근 오차)
#      + RMSE 값이 낮을수록 모형의 정확도가 높다. 
#      + MSE의 양의 제곱근이다 
#      ==> rmse(actual, predicted)
#

library(Metrics)

y_true = c(3,5,7,9)
y_pred = c(2,5,8,10)

mse(y_true, y_pred)
rmse(y_true, y_pred)

#   3) 결정 계수(Coefficient of Determination: R^2)
#     - 선형 회귀 분석의 성능 검증지표로 많이 이용(선형이 아닌 회귀모형에서도 사용 가능)    
#     - 회귀모형이 실제값을 얼마나 잘 나타내는지에 대한 비율
#     - 결정 계수가 1에 가까울수록 실제값을 잘 설명한다 (값의 범위: 0 <= R^2 <= 1)
#     - summary 함수를 이용하면 출력할 수 있다.
#

x = c(3,5,7,9)
y = c(2,5,8, 10)

df = data.frame(x, y)
md = lm(y~x, df)
summary(md)
md

#
# (2) 분류모형 평가
#    - 구축한 회귀부형에 대한 평가에 혼동 행렬(Confusion Matrix)과 
#      AUC(Area Under ROC)등을 이용할 수 있다. 
#
#   1) predict 함수 
#      - predict 함수는 새로운 입력 데이터에 대한 에측값을 반환하는 함수이다.
#       ==> predict(object, newdata, probability)
#
#   2) 혼동 행렬
#      - 혼동 행렬을 분석 모델에서 구한 분류의 예측 범주와 데이터의 실제 분류 범주를
#        교차표(Cross table) 형태로 정리한 행렬이다.
#      - 혼동 행렬 함수  
#        ==> confusionMatrix 함수는 실제값과 예측값의 벡터로 혼동 행렬을 구하여 
#            분류 모델의 학습 성능을 평가하기 위한 함수이다.
#        ==> confusionMatrix(예측 데이터, 실제 분류 데이터) 
#    3) 혼동 행렬을 통한 분류 모형의 평가지표
#      - 혼동 행렬로부터 계산될 수 있는 평가지표는 정확도, 오차 비율, 민감도 등이 있고, 
#        그 중에서 정확도, 민감도, 정밀도는 많이 사요오디는 지표이다. 
#         
#        + 정확도(Accuracy) 
#           ++ 정확도는 실제 분류 범주를 정확하게 예측한 비율이다. 
#           ++ 전체 예측에서 TP와 TN이 차지하는 비율이다.
#
#              (TP+TN) / (TP+TN+FP+FN)
#
#         + 재현율(Recall) = 민감도(Sensitivity) 
#           ++ 실제로 "긍정"인 번주에서 "긍정을 올바르게 예측(TP)한 비율
#
#            TP / (TP+TN)
#
#         + 정밀도(Precision)
#           ++  "긍정"으로 예측한 비율 중에서 실제로 "긍정(TP)"인 비율이다. 
#        
#           TP / (TP+NP)
#            
#         + F1 지표(F1-Score) 
#           ++ F1 지표는 정밀도와 민감도(재현율)를 하나로 합한 성능평가지표이다.
#           ++ 정밀도와 민감도 양쪽이 모두 클 때 F1 지표도 큰 값을 가진다. (0~1 사이의 범위)
#
#                     Precision  X  Recall  
#            2 x  --------------------------------
#                     Precision  +  Recall  

library(caret)

y_true = c(1, 0, 1, 0, 1)
y_pred = c(1, 1, 1, 0, 0)

cm = confusionMatrix(factor(y_pred), factor(y_true))
print(cm)
print(cm$byClass)

#
# (2) AUC
#    - AUC는 ROC 곡선(Receiver Operating Characterisitic curve)의 아랫부분의 면적이다. 
#    - AUC 값은 항상 0.5~1의 값을 가지며 1에 가까울수록 좋은 모형이다. 
#
#   1) AUC 함수
#      - ModelMetrics 패키지의 auc 함수를 이용하여 구할 수 있다. 
#       ==> auc(y_true, y_pred)
#       

library(ModelMetrics)

y_true = c(1, 0, 1, 0, 1)
y_pred = c(1, 1, 1, 0, 0)

auc(y_true, y_pred)

