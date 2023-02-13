import streamlit as st
import sys
import re
import matplotlib.pyplot as plt
from PIL import Image

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

def occurrence_check(prefix, string_list):
    return sum(prefix in s for s in string_list)

def session_state_cut(ss_dict, prefix, number_widgets): #recebe o dicionario de session state, o prefixo da key e o numero de widgets
    occur_ses_state = list(s for s in list(ss_dict) if s.startswith(prefix)) #pegado as ocorrencias da key no dicionario
    sorted_list = sorter(occur_ses_state) #deixa a lista acima em ordem alfanumérica
    reversed_list = sorted_list[::-1] #invertendo a lista acima
    dif = occurrence_check(prefix, list(ss_dict)) - number_widgets #o numero de keys excedentes é a diferença entre o numero de ocorrencias no 
                                                                    #dict de session state e o numero de widgets
    elements_to_cut = list() #lista pra retornar as keys excedentes

    for i in range(dif):
        elements_to_cut.append(reversed_list[i])
    return elements_to_cut

def plot_results(
    y=None,
    *,
    yhat=None,
    figsize=(8, 5),
    n=100,
    style="seaborn-white",
    facecolor="white",
    title="Free run simulation"
):
    plt.style.use(style)
    plt.rcParams["axes.facecolor"] = facecolor
    fig, ax = plt.subplots(figsize=figsize, facecolor=facecolor)
    ax.plot(y[:n], c="#1f77b4", alpha=1, marker="o", label="Data", linewidth=1.5)
    ax.plot(yhat[:n], c="#ff7f0e", marker="*", label="Model", linewidth=1.5)

    ax.set_title(title, fontsize=18)
    ax.legend()
    ax.tick_params(labelsize=14)
    ax.set_xlabel("Samples", fontsize=14)
    ax.set_ylabel("y, $\hat{y}$", fontsize=14)

    fig.savefig('temp_figs//results_fig.png', bbox_inches='tight')
    image = Image.open('temp_figs//results_fig.png')
    return image

def plot_residues_correlation(
    data=None,
    *,
    figsize=(8, 5),
    n=100,
    style="seaborn-white",
    facecolor="white",
    title="Residual Analysis",
    ylabel="Correlation",
    second_fig = False
):
    plt.style.use(style)
    plt.rcParams["axes.facecolor"] = facecolor
    fig, ax = plt.subplots(figsize=figsize, facecolor=facecolor)
    ax.plot(data[0], color="#1f77b4")
    ax.axhspan(data[1], data[2], color="#ccd9ff", alpha=0.5, lw=0)
    ax.set_xlabel("Lag", fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.tick_params(labelsize=14)
    ax.set_ylim([-1, 1])
    ax.set_title(title, fontsize=18)

    if second_fig == True:
        fig.savefig('temp_figs//residues_fig_2.png', bbox_inches='tight')
        image = Image.open('temp_figs//residues_fig_2.png')
    else:
        fig.savefig('temp_figs//residues_fig_1.png', bbox_inches='tight')
        image = Image.open('temp_figs//residues_fig_1.png')
    return image

def adjust_string(label_string):
    spaced_string = ' '.join(label_string.split('_'))
    return spaced_string.capitalize()

def get_acronym(string):
    oupt = string[0]
    
    for i in range(1, len(string)):
        if string[i-1] == ' ':
            oupt += string[i]
    return oupt.upper()

def get_lags_list(n):
    lags = []
    for i in range(1,n+1):
        lags.append(i)
    return lags