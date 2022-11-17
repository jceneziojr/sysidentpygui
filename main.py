#os comentários não são feitos do modo usual (usando as aspas e varias linhas), pois o streamlit interpreta o texto solto no código 
#entre aspas como string, e 'printa' o texto na aplicação

import streamlit as st
import os 
import pandas as pd
from assist.assist_dicts import basis_function_list, basis_function_parameter_list, model_struc_dict, model_struc_selec_parameter_list, ic_list, estimators_list, model_type_list
import assist.utils as utils
import importlib
from sysidentpy.basis_function import *
import numpy as np
from sysidentpy.utils.generate_data import get_siso_data
from sysidentpy.metrics import root_relative_squared_error
root = os.path.join(os.path.dirname(__file__)+'\\assist')
path = os.path.join(root, "pagedesign.py")

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())
tabl = ['Load Data', 'Model Setup', 'Model Validation and Metrics', 'Save Model']

tab1, tab2, tab3, tab4 = st.tabs(tabl)

x_train, x_valid, y_train, y_valid = get_siso_data(
    n=1000,
    colored_noise=False,
    sigma=0.0001,
    train_percentage=90)

with tab1:
    col1, esp1, col2 = st.columns([5,1,5])

    with col1:
        st.file_uploader("Data", key='id_data', help='Upload your  file')
        if st.session_state['id_data'] != None:
            data_id = pd.read_csv(st.session_state['id_data'], sep=' ')
        #data_id

    st.markdown("""---""")

with tab2:
    st.number_input('Validating Percentage', 0.0, 100.0, value=15.0, key='val_perc')
    st.markdown("""---""")

    st.selectbox('Basis Function', basis_function_list, key='basis_function_key') #escolhendo a basis function
    
    for i in range(len(basis_function_list)): #pra saber quantos widgets devem ser criados, é preciso que a gente saiba qual basis function foi escolhida,  
                                        #então a variável i serve pra checarmos isso

        if st.session_state['basis_function_key'] == basis_function_list[i]: #se a basis function escolhida for a mesma da iteração atual, segundo i, roda o código
                                                            #criando os widgets
            wcont1 = 0 #variável de assistência pra criar os widgets recursivamente
            key_list = list(basis_function_parameter_list[i]) #essa lista das keys do dict de parametros, serve para acessar os values e ser a label dos widgets
            while wcont1<len(utils.dict_values_to_list(basis_function_parameter_list[i])): #criando os widgets recursivamente, e atribuindo os nomes p/ os widgets
                k = 'bf_par_' + str(wcont1)
                # st.write(isinstance(basis_function_parameter_list[i][key_list[wcont1]], bool))
                if isinstance(basis_function_parameter_list[i][key_list[wcont1]], int):
                    if isinstance(basis_function_parameter_list[i][key_list[wcont1]], bool):
                        st.write(key_list[wcont1])
                        st.checkbox('', key = k, value=basis_function_parameter_list[i][key_list[wcont1]]) #no checkbox, a label é automaticamente a direita, então
                                                                                #chamo antes em cima
                    else:
                        st.number_input(key_list[wcont1], key = k, min_value=0, value=basis_function_parameter_list[i][key_list[wcont1]])
                        
                if isinstance(basis_function_parameter_list[i][key_list[wcont1]], float):
                    st.number_input(key_list[wcont1], key = k, min_value=0.0, value=basis_function_parameter_list[i][key_list[wcont1]])

                if isinstance(basis_function_parameter_list[i][key_list[wcont1]], str):
                    st.write('string') 

                wcont1 = wcont1+1

            bf_par_dict = dict(basis_function_parameter_list[i]) #aqui ele copia o dicionario base dos parametros, para assim substituir com os valores novos 
                                                    #obtidos no widget
            bf_par_list = list() #lista p/ pegar as keys dos widgets e podermos atribuir os valores corretos ao dict acima

            for j in range(len(list(st.session_state))): #pegando as keys de session state que tem o nome base para ser widget dos parametros de basis function
                if list(st.session_state)[j].startswith('bf_par_'): 
                    bf_par_list.append(list(st.session_state)[j])

                    #o streamlit, ele "demora um clique" pra resetar os session states, precisava
                    #fazer um jeito de deletar os que são atribuidos aos widgets para n dar o erro de
                    #list index out of range

            bf_par_list = sorted(bf_par_list) #a lista precisa estar em ordem alfabética para o próximo bloco

            for j in range(len(bf_par_list)): #refazendo o dicionário para os argumentos do objeto da basis function
                bf_par_dict[list(basis_function_parameter_list[i])[j]] = st.session_state[bf_par_list[j]] 
        
            st.write(bf_par_dict)
    st.markdown("""---""")
    
    bf_module = importlib.import_module('sysidentpy.basis_function._basis_function') #pegando o arquivo onde tá a classe da basis function
    bf = utils.str_to_class(st.session_state['basis_function_key'], bf_module)(**bf_par_dict) #instanciando a basis function

    st.selectbox('Model Structure Selection Algorithm', list(model_struc_dict), key='model_struc_select_key')
    

    for i in range(len(model_struc_dict)):

        if st.session_state['model_struc_select_key'] == list(model_struc_dict)[i]: 
		
            wcont2 = 0 
            key_list = list(model_struc_selec_parameter_list[i]) 
            while wcont2<len(utils.dict_values_to_list(model_struc_selec_parameter_list[i])):
                k = 'mss_par_' + str(wcont2)

                if isinstance(model_struc_selec_parameter_list[i][key_list[wcont2]], int):
                    if isinstance(model_struc_selec_parameter_list[i][key_list[wcont2]], bool):
                        st.write(key_list[wcont2])
                        st.checkbox('', key = k, value=model_struc_selec_parameter_list[i][key_list[wcont2]]) 
                    else:
                        if model_struc_selec_parameter_list[i][key_list[wcont2]]<0:
                            st.number_input(key_list[wcont2], key = k, min_value=-50, value=model_struc_selec_parameter_list[i][key_list[wcont2]])
                        else:
                            st.number_input(key_list[wcont2], key = k, min_value=0, value=model_struc_selec_parameter_list[i][key_list[wcont2]])

                if model_struc_selec_parameter_list[i][key_list[wcont2]] is None:
                    # st.number_input(key_list[wcont2], key = k, min_value=-50, value=model_struc_selec_parameter_list[i][key_list[wcont2]])
                    st.write('Tipo None AQUI') #n ta funcionando n

                if isinstance(model_struc_selec_parameter_list[i][key_list[wcont2]], float):
                    if model_struc_selec_parameter_list[i][key_list[wcont2]]<0.0:
                        st.number_input(key_list[wcont2], key = k, min_value=-50.0, value=model_struc_selec_parameter_list[i][key_list[wcont2]])
                    else:
                        st.number_input(key_list[wcont2], key = k, min_value=0.0, value=model_struc_selec_parameter_list[i][key_list[wcont2]])
                                                                                                   
                if isinstance(model_struc_selec_parameter_list[i][key_list[wcont2]], str):
                    if key_list[wcont2] == 'info_criteria':
                        st.selectbox(key_list[wcont2], ic_list, key = k)
                    if key_list[wcont2] == 'estimator':
                        st.selectbox(key_list[wcont2], estimators_list, key = k)
                    if key_list[wcont2] == 'model_type':
                        st.selectbox(key_list[wcont2], model_type_list, key = k)

                wcont2 = wcont2+1

            model_struc_selec_par_dict = dict(model_struc_selec_parameter_list[i]) 
            model_struc_selec_par_list = list() 

            for j in range(len(list(st.session_state))):
                if list(st.session_state)[j].startswith('mss_par_'): 
                    model_struc_selec_par_list.append(list(st.session_state)[j])
            model_struc_selec_par_list = utils.sorter(model_struc_selec_par_list)
            st.write(model_struc_selec_par_list)
            for j in range(len(model_struc_selec_par_list)):
                model_struc_selec_par_dict[list(model_struc_selec_parameter_list[i])[j]] = st.session_state[model_struc_selec_par_list[j]] 
            model_struc_selec_par_dict['basis_function'] = bf
            st.write(model_struc_selec_par_dict)
    st.markdown("""---""")

    model_struc_selec_module = importlib.import_module('sysidentpy.model_structure_selection'+'.'+model_struc_dict[st.session_state['model_struc_select_key']][0])
    model = utils.str_to_class(model_struc_dict[st.session_state['model_struc_select_key']][1], model_struc_selec_module)(**model_struc_selec_par_dict)
    model.fit(X=x_train, y=y_train)
    yhat = model.predict(X=x_valid, y=y_valid)
    rrse = root_relative_squared_error(y_valid, yhat)
    st.write(rrse)