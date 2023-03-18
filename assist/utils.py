import streamlit as st
import sys
import re
import matplotlib.pyplot as plt
from PIL import Image
from sysidentpy.utils.display_results import results
import pandas as pd
import inspect

def addlogo():
    st.markdown("""<img src="https://i.imgur.com/roD5DkG.png" alt="logo" class="center"> """, unsafe_allow_html=True) #adiciona a logo
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

def get_estimators(cls):   
    return [i for i in cls.__dict__.keys() if i[:1] != '_']

def get_default_args(func):
    """
    Returns a dictionary containing the default arguments of the given function.
    """
    sig = inspect.signature(func)
    return {
        arg.name: arg.default
        for arg in sig.parameters.values()
    }

def get_model_struc_dict(module, prefix): #creates a dictionary that the app uses for the method name and objects instantiating
    _model_struc_dict = dict()
    _cls_names = [cls_name for cls_name,_ in inspect.getmembers(module, lambda member: inspect.isclass(member))]
    _cls_modules_paths = [getattr(module, classname).__module__ for classname in _cls_names]
    _module_names = [modpath.replace(prefix,'') for modpath in _cls_modules_paths]

    for i in range(len(_cls_names)):
        if _cls_names[i] == 'FROLS':
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+' Compact)'] = [_module_names[i],_cls_names[i]]
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+' Complete)'] = [_module_names[i],_cls_names[i]]
        elif _cls_names[i] == 'MetaMSS':
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+' Compact)'] = [_module_names[i],_cls_names[i]]
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+' Complete)'] = [_module_names[i],_cls_names[i]]
        elif _cls_names[i] == 'ER':
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+' Compact)'] = [_module_names[i],_cls_names[i]]
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+' Complete)'] = [_module_names[i],_cls_names[i]]
        else:
            _model_struc_dict[adjust_string(_module_names[i])+' ('+_cls_names[i]+')'] = [_module_names[i],_cls_names[i]]
    
    return _model_struc_dict

def get_model_struc_selec_parameter_list(module):
    _cls_names = [cls_name for cls_name,_ in inspect.getmembers(module, lambda member: inspect.isclass(member))]
    _model_struc_selec_parameter_list = list()
    for _cls in _cls_names:
        if _cls == 'FROLS':
            _full_args = get_default_args(getattr(module, _cls))
            _compact_form_keys =['order_selection', 'n_terms', 'n_info_values', 'extended_least_squares', 'ylag', 'xlag', 'info_criteria','estimator', 'model_type', 'basis_function']
            _compact_args = dict( ((key, _full_args[key]) for key in _compact_form_keys) )
            _model_struc_selec_parameter_list.append(_compact_args)
            _model_struc_selec_parameter_list.append(_full_args)
        elif _cls == 'MetaMSS':
            _full_args = get_default_args(getattr(module, _cls))
            _compact_form_keys =['maxiter', 'k_agents_percent', 'norm', 'n_agents', 'xlag', 'ylag', 'estimator', 'estimate_parameter', 'loss_func', 'model_type', 'basis_function']
            _compact_args = dict( ((key, _full_args[key]) for key in _compact_form_keys) )
            _model_struc_selec_parameter_list.append(_compact_args)
            _model_struc_selec_parameter_list.append(_full_args)
        elif _cls == 'ER':
            _full_args = get_default_args(getattr(module, _cls))
            _compact_form_keys =['ylag', 'xlag', 'estimator', 'k', 'n_perm', 'skip_forward', 'model_type', 'basis_function']
            _compact_args = dict( ((key, _full_args[key]) for key in _compact_form_keys) )
            _model_struc_selec_parameter_list.append(_compact_args)
            _model_struc_selec_parameter_list.append(_full_args)
        else:   
            _model_struc_selec_parameter_list.append(get_default_args(getattr(module, _cls)))

    return _model_struc_selec_parameter_list

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

def get_model_eq(model):
    r = pd.DataFrame(
        results(
            model.final_model, model.theta, model.err,
            model.n_terms, err_precision=8, dtype='sci'
        ),
        columns=['Regressors', 'Parameters', 'ERR'])

    model_string = 'y_k = '
    for ind in r.index:
        model_string += f'  {float(r.iat[ind, 1]):.2f}*{r.iat[ind, 0]}'
        if len(r.index) != ind+1:
            model_string += '+'
    model_string = model_string.replace('(', '_{')
    model_string = model_string.replace(')', '}')
    return model_string