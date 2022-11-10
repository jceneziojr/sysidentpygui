import streamlit as st
import sys
import re

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

def splitter(string_list):
    splitted_list = list()
    for i in range(len(string_list)):
        splitted_list.append(list(filter(None, re.split(r'\D', string_list[i]))))
        splitted_list[i] = int(splitted_list[i][0])
    return splitted_list

def sorter(string_list):
    splitted_list = splitter(string_list)
    sorted_number_list = sorted(splitted_list)
    sorted_list = [0]*len(string_list)
    for i in range(len(string_list)):
        sorted_list[i] = string_list[splitted_list.index(sorted_number_list[i])]
    return sorted_list