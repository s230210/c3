# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl') 

# 2. 모델 설명
st.title('하루 게시물 수에 따른 팔로워수 증가 예측 모델')
col1, col2,col3 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 선형 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 700건')
      st.write(' - 테스트 데이터 : 300건')
      st.write(' - 모델 정확도 : 0.0') 

