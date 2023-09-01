# -*- coding:utf-8 -*-

import streamlit as st
from eda_app import run_eda_app

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
        st.subheader('머신러닝')
    elif choice == 'About':
        st.subheader('About')
    else:
        pass

if __name__ == "__main__":
    main()