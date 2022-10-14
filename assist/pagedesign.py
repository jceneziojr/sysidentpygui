import streamlit as st
import assist.utils as utils

st.set_page_config( #Configurações gerais da página
    page_title="SysIdentPyGUI",
    page_icon="http://sysidentpy.org/overrides/assets/images/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

utils.addlogo()
utils.removemenu()
