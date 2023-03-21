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

<img src="/images/1.PNG" width="60%" height="60%" />

Then, go to the 'Model Setup' tab and make your desired changes to the model configuration. At the bottom of the page, you can make changes to the way that SysIdentPy will run the predict if wanted.

<img src="/images/2.PNG" width="60%" height="60%" />
For MISO data, you can define the lags for each specific input separately.

<img src="/images/3.PNG" width="60%" height="60%" />
You can then proceed to the 'Model Validation and Metrics' tab, to check the model regressors, results and residues plots, as well as the metrics.

<img src="/images/4.PNG" width="60%" height="60%" />
<img src="/images/5.PNG" width="60%" height="60%" />
<img src="/images/6.PNG" width="60%" height="60%" />

#### Model download
Go to the 'Save Model' tab to save your final model.

<img src="/images/7.PNG" width="60%" height="60%" />

#### Load Model
Go to the 'Load Model' page and load your data files and the model file you saved before.

<img src="/images/8.PNG" width="60%" height="60%" />

After loaded, you can visualize the regressors and metrics table, as well as the results and residues plots. Notice, that you can use a new dataset to check the model acuracy.

<img src="/images/9.PNG" width="60%" height="60%" />

#### Simulate model

Go to the 'Simulate a predefined model' page, and load your test data.

<img src="/images/10.PNG" width="60%" height="60%" />

Then set the nonlinearity degree of the model and prepare the regressors list (as exemplified in the [tutorial](https://sysidentpy.org/examples/simulating_a_predefined_model/)), adding each group by itself. If needed, delete the list and start over.

<img src="/images/11.PNG" width="60%" height="60%" />

Set the model parameters.

<img src="/images/12.PNG" width="60%" height="60%" />

Set the simulation options if wanted, and then hit the 'Simulate the model' button.

<img src="/images/13.PNG" width="60%" height="60%" />

Go further down to see the model equation, model metrics, results and residues plots.

<img src="/images/14.PNG" width="60%" height="60%" />

## Why does SysIdentPyGUI exist?

SysIdentPyGUI is an use alternative for people that would like to use SysIdentPy toolbox but aren't familiar with Python, such as medical or economy students.
