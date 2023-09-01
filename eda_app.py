# -*- coding:utf-8 -*-

import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_eda_app():

    st.subheader('탐색적 자료 분석 페이지')
    st.subheader('잘 실행되는 중...')

    iris_df  = pd.read_csv('data/iris.csv')

    # 메뉴지정
    submenu = st.sidebar.selectbox('submenu', ['통계', '시각화', '그래프'])
    if submenu == '통계':
        st.subheader('통계')
        st.dataframe(iris_df)
    elif submenu == '시각화':
        st.subheader('시각화')
    elif submenu == '그래프':
        st.subheader('그래프')
    else:
        pass

    