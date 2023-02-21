import streamlit as st
from sysidentpy.utils.save_load import load_model
from sysidentpy.utils.display_results import results
from sysidentpy.simulation import SimulateNARMAX
from sysidentpy.basis_function._basis_function import Polynomial
from sysidentpy.residues.residues_correlation import compute_residues_autocorrelation, compute_cross_correlation
from sysidentpy.metrics import __ALL__ as metrics_list
import sysidentpy.metrics as metrics
import os
import sys
sys.path.insert(1, os.path.dirname(__file__).replace('\pages',''))
import assist.utils as utils
import pandas as pd
import pickle as pk
import numpy as np

root = os.path.join(os.path.dirname(__file__).replace('\pages','')+'\\assist')
path = os.path.join(root, "pagedesign.py")

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())

def add_regressors(regr_index_key, regr_list_key): #adiciona um grupo de regressores ao session_state específico
    regkeys = utils.sorter([regk for regk in list(st.session_state) if regr_index_key in regk]) #por segurança, deixa as keys de cada regressor do grupo em ordem alfanumérica
    nested_regressors = [st.session_state[regk] for regk in regkeys] #pega os valores correspondentes de cada key no dict session_state e coloca na lista do grupo de regressores
    st.session_state[regr_list_key].append(nested_regressors) #faz o append da lista do grupo de regressores na lista 'geral' de regressores

def add_thetas(thetas_index_key, thetas_list_key): #o código é semelhante ao acima, a diferença é a última linha
    thetaskeys = utils.sorter([thetask for thetask in list(st.session_state) if thetas_index_key in thetask])
    nested_thetas = [st.session_state[thetask] for thetask in thetaskeys]
    st.session_state[thetas_list_key] = nested_thetas #aqui é feita uma atribuição ao invés de append

col2, esp1, col3 = st.columns([5,1,5])

if 'regr_list' not in st.session_state:
    st.session_state['regr_list'] = list() #lista 'geral' para armazenar todos os grupos de regressores
    
if 'thetas_list' not in st.session_state:
    st.session_state['thetas_list'] = list() #lista para armazenar os thetas referentes a cada grupo de regressores

with col2:
    st.file_uploader("Test Input Data", key='tx_data', help='Upload your CSV file')
    if st.session_state['tx_data'] != None:
        x_test = pd.read_csv(st.session_state['tx_data'], sep='\t', header=None).to_numpy()

with col3:
    st.file_uploader("Test Output Data", key='ty_data', help='Upload your CSV file')
    if st.session_state['ty_data'] != None:
        y_test = pd.read_csv(st.session_state['ty_data'], sep='\t', header=None).to_numpy()

st.markdown("---")

st.write('Define your model (check the [tutorial](https://sysidentpy.org/examples/simulating_a_predefined_model/))')

st.write('Insert the regressors codification (the order of the codes must be the same as the one in the tutorial)')

col4, esp2, esp3 = st.columns([3, 1, 10])

with col4:
    st.number_input('Nonlinear degree', key='nonl_deg', min_value=1, value=2)
    
col5, esp4, col6, esp5 = st.columns([3,2,5,5])      
    
with col5:
    with st.form('Reg form'):
        for reg_input_number in range(st.session_state['nonl_deg']):
            st.number_input('Regressor '+str(reg_input_number+1), key='reg_'+str(reg_input_number+1), min_value=0, value=0)
        add_reg = st.form_submit_button('Add regressors')

        if add_reg:
            add_regressors('reg_', 'regr_list')

    model_code_l = np.array(st.session_state['regr_list'])
    clear_regr = st.button('Clear regressors list')
    if clear_regr:
        st.session_state['regr_list'].clear()

    with st.form('Theta form'):
        for numb_theta in range(model_code_l.shape[0]):
            st.number_input('Parameter value for regressor group '+str(numb_theta+1), key='theta_'+str(numb_theta+1), value=1.0e0, format='%e')
        add_theta = st.form_submit_button('Set Parameters')

        if add_theta:
            add_thetas('theta_', 'thetas_list')
    theta_l = np.array([st.session_state['thetas_list']]).T
    clear_thetas = st.button('Clear parameters list')
    if clear_thetas:
        st.session_state['thetas_list'].clear()

    
with col6:
    st.caption('Regressors groups')
    for regr_text in st.session_state['regr_list']:
        st.text(str(regr_text))  

col7, esp6, esp7 = st.columns([3, 1, 5])    
if st.session_state['tx_data'] != None and st.session_state['ty_data'] !=None:

    with col7:
        if 'steps_ahead' not in st.session_state:
            st.session_state['steps_ahead'] = None
        st.write('Free Run Simulation')
        if st.checkbox('', value=True, key='free_run') is False:
            st.number_input('Steps Ahead', key = 'steps_ahead', min_value=1)
        with st.form('Simulate'):
            st.write('Calculate ERR')
            st.checkbox(' ', key='calc_err', value=True)
            st.write('Estimate parameter')
            st.checkbox(' ', key='estimate_par', value=False)
            st.write('Extended least squares')
            st.checkbox(' ', key='extend_least_squares', value=True)
            st.markdown("---")
    
            st.write()
            sim_model = st.form_submit_button('Simulate the model', help='This button will work only if your data is loaded and the regressors/parameters are properly set!')
    
    
    st.markdown("---")

    if sim_model==True:
        sim = SimulateNARMAX(basis_function=Polynomial(), calculate_err=st.session_state['calc_err'], estimate_parameter=st.session_state['estimate_par'], extended_least_squares=st.session_state['extend_least_squares'])
        yhat_sim = sim.simulate(
            X_test = x_test,
            y_test = y_test,
            model_code = model_code_l,
            theta = theta_l,
            steps_ahead = st.session_state['steps_ahead']
        )
        st.write('Model equation:')
        st.latex(utils.get_model_eq(sim))

        metrics_df = dict()
        metrics_namelist = list() 
        metrics_vallist = list() #criando listas separadas deixa mais bonito
        with st.expander('Metrics'):
            for index in range(len(metrics_list)):
                if metrics_list[index] == 'r2_score' or metrics_list[index] == 'forecast_error':
                    pass
                else:
                    metrics_namelist.append(utils.get_acronym(utils.adjust_string(metrics_list[index])))
                    metrics_vallist.append(getattr(metrics, metrics_list[index])(y_test, yhat_sim))
            metrics_df["Metric Name"] = metrics_namelist
            metrics_df["Value"] = metrics_vallist
            st.dataframe(pd.DataFrame(metrics_df))

        with st.expander('Results Plot'):
            st.image(utils.plot_results(y=y_test, yhat=yhat_sim, n=1000))

        ee = compute_residues_autocorrelation(y_test, yhat_sim)
        if x_test.shape[1]==1:
            x1e = compute_cross_correlation(y_test, yhat_sim, x_test)
        else:
            x1e = compute_cross_correlation(y_test, yhat_sim, x_test[:, 0])

        with st.expander('Residues Plot'):
            st.image(utils.plot_residues_correlation(data=ee, title="Residues", ylabel="$e^2$"))
            st.image(utils.plot_residues_correlation(data=x1e, title="Residues", ylabel="$x_1e$", second_fig=True))
