<p align="center">
  <img src="img/logo_white.png" alt= “” class=“center” width="50%" height="50%">
</p>

# Welcome to SysIdentPyGUI documentation

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sysidentpygui.streamlit.app/)
[![Repo](https://badgen.net/github/release/wilsonrljr/sysidentpy/?icon=github&labelColor=373736&label&color=f47c1c)](https://github.com/wilsonrljr/sysidentpy)
[![Repo](https://badgen.net/github/release/jceneziojr/sysidentpygui/stable?label&color=f47c1c&labelColor=373736&icon=github)](https://github.com/jceneziojr/sysidentpygui)
## Introduction

In this website is presented the documentation for SysIdentPyGUI, the graphical user interface for system identification using SysIdentPy. Here the user can learn through examples how to use the webapp for system identification and simulation in a variety of ways.

Through SysIdentPyGUI, a system can be identified using NARMAX models, with Polynomial or Fourier basis functions, using advanced structure selection algorithms (FROLS, AOLS, MetaMSS or ER), combined with a wide range of metrics for posterior analysis and many other costumizable parameters.

The user can also load a previously identified model, to validate and predict using a separate dataset, as well as simulating a predefined model through its equation.

SysIdentPyGUI has an user friendly and straightforward interface, so that anyone can bring up their input and output data, and easily get a non-linear mathematical model that can describe their behaviour.
## Usage

SysIdentPyGUI is currently hosted on [***Streamlit Cloud***](https://sysidentpygui.streamlit.app/). You can run it locally on your machine via a containerized version through [***Docker***](https://www.docker.com/) by using the Dockerfile that is available, through the following commands:

``` console
docker build -t sysidenpygui .
```
The above command will build the Docker Image. Check the image by typing:

``` console
docker images
```

The `sysidentpygui` image should appear in the images list. Run the container with:

``` console
docker run -p 8501:8501 sysidentpygui
```

Alternatively, you can run the Streamlit application locally using:

``` console
streamlit run 1_🔎_SysIdentPyGUI.py
```

### Requirements for local use

SysIdentPyGUI requires the following modules for a local host:

- Python (>= 3.10)
- Sysidentpy (>= 0.3.1)
- Streamlit (>= 1.14.0)
- Matplotlib (>= 3.6.1)
- Numpy (>= 1.23.4)
- Pandas (>= 1.5.1)
- Pillow (>= 9.4.0)

Use `pip` to install the dependecies throught the `requirements.txt` file. If you choose to run the containerized version, the Dockerfile will install de dependencies for you.