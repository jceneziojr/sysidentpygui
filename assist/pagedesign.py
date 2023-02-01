import streamlit as st
import assist.utils as utils

st.set_page_config( #Configurações gerais da página
    page_title="SysIdentPyGUI",
    page_icon="http://sysidentpy.org/overrides/assets/images/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    
)

utils.addlogo()
utils.removemenu()

with st.sidebar:
    st.write("SysIdentPy is an open-source Python module for System Identification using NARMAX models built on top of numpy and is distributed under the 3-Clause BSD license. SysIdentPy provides an easy-to-use and flexible framework for building Dynamical Nonlinear Models for time series and dynamic systems.")
    st.write("Check our [documentation](https://sysidentpy.org/) and our GitHub repository!")