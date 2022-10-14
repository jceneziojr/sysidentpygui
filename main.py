import streamlit as st
import os 
import pandas as pd
from assist.assist_dicts import bas_fun_list, par_list, model_struc_dict
import assist.utils as utils
import importlib
from sysidentpy.basis_function import *

root = os.path.join(os.path.dirname(__file__)+'\\assist')
path = os.path.join(root, "pagedesign.py")

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())
tabl = ['Load Data', 'Model Setup', 'Model Validation and Metrics', 'Save Model']

tab1, tab2, tab3, tab4 = st.tabs(tabl)

with tab1:
    col1, esp1, col2 = st.columns([5,1,5])

    with col1:
        st.file_uploader("Identification Data", key='id_data', help='Upload your  file')
        if st.session_state['id_data'] != None:
            data_id = pd.read_csv(st.session_state['id_data'], sep=' ')
        #data_id
    with col2:
        st.file_uploader("Validation Data", key='val_data', help='Upload your  file')

    st.markdown("""---""")

with tab2:
    st.selectbox('Basis Function', bas_fun_list, key='bas_fun') #escolhendo a basis function

    for i in range(len(bas_fun_list)): #pra saber quantos widgets devem ser criados, é preciso que a gente saiba qual foi escolhido, então 
                                        #a variável i serve pra checarmos isso

        if st.session_state['bas_fun'] == bas_fun_list[i]: #se a basis function escolhida for a mesma da iteração atual, segundo i, roda o código
                                                            #criando os widgets
            wcont1 = 0 #variável de assistência pra criar os widgets recursivamente
            key_list = list(par_list[i]) #essa lista das keys do dict de parametros, serve para acessar os values e ser a label dos widgets
            while wcont1<len(utils.dict_values_to_list(par_list[i])):
                k = 'bf_par_' + str(wcont1)

                if type(par_list[i][key_list[wcont1]]) is int:
                    st.number_input(key_list[wcont1], key = k, min_value=0, value=par_list[i][key_list[wcont1]])

                if type(par_list[i][key_list[wcont1]]) is float:
                    st.number_input(key_list[wcont1], key = k, min_value=0.0, value=par_list[i][key_list[wcont1]])

                if type(par_list[i][key_list[wcont1]]) is bool:
                    st.write(key_list[wcont1].capitalize()) #ver o padrão dos nomes dos parametros, para ser capitalizados etc
                    st.checkbox('', key = k, value=par_list[i][key_list[wcont1]]) #no checkbox, a label é automaticamente a direita, então
                                                                                #chamo antes em cima

                if type(par_list[i][key_list[wcont1]]) is str:
                    st.write('string') 

                wcont1 = wcont1+1
            bf_par_dict = par_list[i]
            bf_par_list = list()
            st.session_state
            for j in range(len(list(st.session_state))): #pegando as keys de session state que tem o nome base para ser widget dos parametros de basis function
                if list(st.session_state)[j].startswith('bf_par_'):
                    bf_par_list.append(list(st.session_state)[j])

            bf_par_list = sorted(bf_par_list) #a lista precisa estar em ordem alfabética para o próximo bloco

            for j in range(len(bf_par_list)): #refazendo o dicionário para os argumentos do objeto da basis function
                
                bf_par_dict[list(par_list[i])[j]] = st.session_state[bf_par_list[j]] 
            st.write('esta acontecendo um bug, que não está atualizando')
            st.write(bf_par_dict)
    st.markdown("""---""")
    
    
    
    st.selectbox('Model Structure Selection Algorithm', list(model_struc_dict), key='model_struc')

    mss_module = importlib.import_module('sysidentpy.model_structure_selection'+'.'+model_struc_dict[st.session_state['model_struc']][0]) #aqui ele faz o preparo para fazer o import da classe específica
    bf_module = importlib.import_module('sysidentpy.basis_function._basis_function')

    bf = utils.str_to_class(st.session_state['bas_fun'], bf_module)(2)

    model = utils.str_to_class(model_struc_dict[st.session_state['model_struc']][1], mss_module)(
        order_selection=True,
        n_info_values=10,
        extended_least_squares=False,
        ylag=2,
        xlag=2,
        info_criteria='aic',
        estimator='least_squares',
        basis_function=bf
    )

    st.write(model)


    # model = utils.str_to_class(sysidentpy.model_structure_selection, forward_regression_orthogonal_least_squares)()
    # model = utils.str_to_class(FROLS, sysidentpy.model_structure_selection)()
    #ver no arquivo oqe.py, parece ter dado certo
# st.write(list(st.session_state))     
# st.write(list(st.session_state)[1].startswith('bf_par_'))



# bf_par_list = list()
# for i in range(len(list(st.session_state))):
#     if list(st.session_state)[i].startswith('bf_par_'):
#         bf_par_list.append(list(st.session_state)[i])

# st.write(bf_par_list)

# for i in range(len(bf_par_list)):
#     st.write(f'{bf_par_list[i]} = {st.session_state[bf_par_list[i]]}')

