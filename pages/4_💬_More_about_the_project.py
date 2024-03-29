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
        "The project idea was initially proposed by [Samir A. M. Martins](https://github.com/samirmartins) and [Wilson R. L. Junior](https://github.com/wilsonrljr) as an alternative for individuals who would like to use the **SysIdentPy** toolbox but are not familiar with Python, such as medical or economics students. However, even experienced users can benefit from its features for quick and easy utilization of the system identification and simulation tools, for example, using a cellphone."
    )
    st.markdown(
        "The concept was then handed to Samir's student [Júlio C. E. Júnior](https://github.com/jceneziojr), who started the development of the web app in the first half of 2022."
    )
    st.markdown(
        "**SysIdentPyGUI** was developed using [Streamlit](https://streamlit.io/) due to its practical syntax, regular updates, and active community."
    )
    st.header("Active Maintainers")
    st.markdown(
        "The project is maintained by Júlio César Enezio Júnior, under the supervision of Wilson Rocha Lacerda Junior and Samir Angelo Milani Martins."
    )
    st.header("Project Status")
    st.markdown(
        "**SysIdentPyGUI** is currently hosted on ***Streamlit Cloud***. A Dockerfile is available in our repository, allowing users to run a local containerized version of the app."
    )
    st.markdown(
        "If you encounter a bug or have a suggestion, please open an issue on our [GitHub repository](https://github.com/jceneziojr/sysidentpygui). We will try to respond to you as soon as possible."
    )
    st.header("Future")
    st.markdown(
        "We aim to make **SysIdentPyGUI** as self-maintaining as possible and keep it up to date with **SysIdentPy**."
    )
    st.markdown(
        "Some features from **SysIdentPy** are not yet available in **SysIdentPyGUI**, such as the Narx Neural Network. However, we are actively analyzing and working towards deploying those features in the future."
    )
    st.header("Contributors")
    st.markdown(
        """<a href="https://github.com/jceneziojr/sysidentpygui/graphs/contributors">
        <img src="https://contributors-img.web.app/image?repo=jceneziojr/sysidentpygui" width = 200/>
        </a>""",
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
    ### Sections
    - [Project History](#project-history)
    - [Active Maintainers](#active-maintainers)
    - [Project Status](#project-status)
    - [Future](#future)
    - [Contributors](#contributors)
    """
    )
