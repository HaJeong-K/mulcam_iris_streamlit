# -*- coding:utf-8 -*-

import streamlit as st
import joblib # 저장할 때 사용
from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    
    st.markdown("# Hello World")
    
    menu = ['Home', 'EDA', '머신러닝', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        st.subheader('Home')
    elif choice == 'EDA':
        # st.subheader('EDA')
        run_eda_app()
    elif choice == '머신러닝':
        run_ml_app()
    elif choice == 'About':
        st.subheader('About')
    else:
        pass

if __name__ == "__main__":
    main()