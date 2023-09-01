# -*- coding:utf-8 -*-

import streamlit as st 

def main():
    
    st.markdown("# Hello World")
    
    menu = ['Home', 'EDA', '머신러닝', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        st.subheader('Home')
    elif choice == 'EDA':
        st.subheader('EDA')
    elif choice == '머신러닝':
        st.subheader('머신러닝')
    elif choice == 'About':
        st.subheader('About')
    else:
        pass

if __name__ == "__main__":
    main()