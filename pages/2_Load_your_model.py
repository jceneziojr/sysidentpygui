import streamlit as st
from sysidentpy.utils.save_load import load_model
from sysidentpy.utils.display_results import results
from sysidentpy.simulation import SimulateNARMAX
from sysidentpy.basis_function._basis_function import Polynomial
from sysidentpy.residues.residues_correlation import compute_residues_autocorrelation, compute_cross_correlation
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

col, esp0, col0 = st.columns([5,1,5])

with col:
    st.file_uploader("Validation Input Data", key='vx_data', help='Upload your CSV file')
    if st.session_state['vx_data'] != None:
        x_valid = pd.read_csv(st.session_state['vx_data'], sep='\t', header=None).to_numpy()

with col0:
    st.file_uploader("Validation Output Data", key='vy_data', help='Upload your CSV file')
    if st.session_state['vy_data'] != None:
        y_valid = pd.read_csv(st.session_state['vy_data'], sep='\t', header=None).to_numpy()

with col:
    st.file_uploader('Load the model file', key='model_file')

if st.session_state['model_file'] != None:
    loaded_model = pk.load(st.session_state['model_file'])

st.markdown("---")

if st.session_state['model_file'] != None and st.session_state['vx_data'] != None and st.session_state['vy_data'] != None:
    yhat_loaded = loaded_model.predict(X=x_valid, y=y_valid)

    r_loaded = pd.DataFrame(results(
        loaded_model.final_model, loaded_model.theta, loaded_model.err,
        loaded_model.n_terms, err_precision=8, dtype='sci'
        ),
    columns=['Regressors', 'Parameters', 'ERR'])
    st.subheader('Model Loaded from file \n')
    st.write(r_loaded)

    with st.expander('Results Plot'):
        st.image(utils.plot_results(y=y_valid, yhat=yhat_loaded, n=1000))