import streamlit as st
import assist.utils as utils


st.set_page_config(  # Configurações gerais da página
    page_title="SysIdentPyGUI",
    page_icon="http://sysidentpy.org/overrides/assets/images/favicon.png",
    layout="wide",
)


utils.addlogo()
utils.removemenu()
st.markdown("---")


col1, esp1, col2 = st.columns([5, 1, 2])
with col1:
    st.header("Project History")
    st.markdown(
        "The project idea was given first by [Samir A. M. Martins](https://github.com/samirmartins) and [Wilson R. L. Junior](https://github.com/wilsonrljr), as an use alternative for people that would like to use **SysIdentPy** toolbox but aren't familiar with Python, such as medical or economy students."
    )
    st.markdown(
        "The concept was then handed to Samir's student [Júlio C. E. Júnior](https://github.com/jceneziojr), who started the development of the web app in the first half of 2022."
    )
    st.markdown(
        "**SysIdentPyGUI** was developed using [Streamlit](https://streamlit.io/) due to its practical syntax, constant updates and active community."
    )
    st.header("Active Maintainers")
    st.markdown(
        "The project is maintained by Júlio César Enezio Júnior, under supervision of Wilson Rocha Lacerda Junior and Samir Angelo Milani Martins."
    )
    st.header("Project Status")
    st.markdown(
        "**SysIdentPyGUI** is currently hosted on ***Streamlit Cloud***. A DockerFile is available in our repository allowing the user to run a local containerized version of the app."
    )
    st.markdown(
        "If you run into a bug or have a suggestion, please open a issue on our [GitHub repository](https://github.com/jceneziojr/sysidentpygui). We will try to answer you as soon as possible."
    )
    st.header("Future")
    st.markdown(
        "We aim to make **SysIdentPyGUI** as self-maintaining as possible and up to date comparing to **SysIdentPy**."
    )
    st.markdown(
        "Some features from **SysIdentPy** aren't available yet, like the Narx Neural Network. But they will be analyzed and deployed eventually."
    )
with col2:
    st.markdown(
        """
    ### Sections
    - [Project History](#project-history)
    - [Active Maintainers](#active-maintainers)
    - [Project Status](#project-status)
    - [Future](#future)
    """
    )
