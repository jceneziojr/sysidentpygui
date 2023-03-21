<p align="center">
<img src="https://i.imgur.com/roD5DkG.png" width="640" height="320" />
</p>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sysidentpygui.streamlit.app/)

## What is SysIdentPyGUI?

**SysIdentPyGUI** is a webapp for the Python module **SysIdentPy**. **SysIdentPy** is an open-source Python module for System Identification using NARMAX models built on top of numpy. **SysIdentPy** provides an easy-to-use and flexible framework for building Dynamical Nonlinear Models for time series and dynamic systems.

Get more information on our [**About**](https://sysidentpygui.streamlit.app/About) page and in [**SysIdentPy's Documentation**](https://sysidentpy.org/) and its [**GitHub repository**](https://github.com/wilsonrljr/sysidentpy/).

## How can I use SysIdentPyGUI?

**SysIdentPyGUI** is currently hosted on [***Streamlit Cloud***](https://sysidentpygui.streamlit.app/). ~You can run it locally on your machine via a containerized version through the Dockerfile that is available~ or by building the Streamlit application using:

``` console
streamlit run 1_SysIdentPyGUI.py
```

### Requirements for local use

SysIdentPyGUI requires the following modules for a local host:

- Python (>= 3.10)
- Sysidentpy (>= 0.2.0)
- Streamlit (>= 1.14.0)
- Matplotlib (>= 3.6.1)
- Numpy (>= 1.23.4)
- Pandas (>= 1.5.1)
- Pillow (>= 9.4.0)

~If you choose to run the containerized version, the Dockerfile will install de dependencies for you.~


## Which features from SysIdentPy are available on SysIdentPyGUI?

- Model identification using AOLS, ER, MetaMSS and FROLS
- Download your model
- Load and validate your model
- Simulate a predefined model

### Basic usage examples
To replicate the following examples, you can download the data available [**here**](https://github.com/jceneziojr/sysidentpygui_testdata).
#### Model ID
First upload your data and set the percentage of data that will be used as validation data.

IMAGEM 1

Then, go to the 'Model Setup' tab and make your desired changes to the model configuration. At the bottom of the page, you can make changes to the way that SysIdentPy will run the predict if wanted.

IMAGEM 2

For MISO data, you can define the lags for each specific input separately.

IMAGEM 3

You can then proceed to the 'Model Validation and Metrics' tab, to check the model regressors, results and residues plots, as well as the metrics.

IMAGEM 4

IMAGEM 5

IMAGEM 6

Go to the 'Save Model' tab to save your final model.

IMAGEM 7


#### Model download
#### Load Model
#### Simulate model

## Why does SysIdentPyGUI exist?

SysIdentPyGUI is an use alternative for people that would like to use SysIdentPy toolbox but aren't familiar with Python, such as medical or economy students.
