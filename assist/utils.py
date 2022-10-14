import streamlit as st
import sys

def addlogo():
    st.markdown("""<img src="https://i.imgur.com/zOcSUib.png" alt="logo" class="center"> """, unsafe_allow_html=True) #adiciona a logo
    st.markdown(""" <style> 
    .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 35%;
    }
    </style>""", unsafe_allow_html=True)

def removemenu(op = True):
    if op == True:
        st.markdown(""" <style> 
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>""", unsafe_allow_html=True)

def dict_key_to_list(g_dict):
    return list(g_dict.keys())

def dict_values_to_list(g_dict):
    return list(g_dict.values()) 

def str_to_class(classname, filepath):
    return getattr(filepath, classname) #pelo jeito, tem q deixar so filepath