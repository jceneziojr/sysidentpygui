---
title: 'SysIdentPyGUI: A Graphical User Interface for System Identification using NARMAX models'
tags:
  - GUI
  - Graphical User Interface
  - Python
  - System Identification
  - NARMAX
  - Dynamical Systems
  - Model Structure Selection
authors:
  - name: Júlio César Enezio Júnior
    orcid: 0009-0005-8510-3432
    corresponding: true
    affiliation: "1" 
  - name: Wilson Rocha Lacerda Junior
    affiliation: "1" 
  - name: Samir Angelo Milani Martins
    orcid: 0000-0003-1702-8504
    affiliation: "1, 2"
affiliations:
 - name: GCoM - Modeling and Control Group at Federal University of São João del-Rei, Brazil
   index: 1
 - name: Department of Electrical Engineering at Federal University of São João del-Rei, Brazil
   index: 2
date: 03 April 2023
bibliography: paper.bib
---

# Summary

The field of System Identification (SI) aims to construct 
mathematical models that describe the static and dynamic behavior 
of systems based on experimental data [@Lju1987]. Nonlinear 
system identification has emerged as a key topic within the SI 
community, and since the 1950s, numerous methods have been 
proposed [@ZAINOL2022106835], [@BONASSI2021547], [@MARTINS2016607], 
[@ayala2020r], [@BBWL2018]. NARMAX (Nonlinear AutoRegressive Moving 
Average with eXogenous input) models are particularly 
well-documented and widely used representations of dynamical 
systems [@Bil2013].

`SysIdentPy` [@Wil2020] is a package designed for system 
identification using polynomial NARMAX models. It has the 
capability to handle both SISO (Single-Input Single-Output) 
and MISO (Multiple-Inputs Single-Output) NARMAX model 
identification, as well as related variants such as 
NARX, NAR, ARMAX, ARX, and AR models. Additionally, 
the package provides several tools for structure selection, 
parameter estimation, and model validation. The package is 
continuously being updated and expanded with new features 
by the community, highlighting its value and importance 
in the field of system identification.

Since `SysIdentPy` is a Python programming tool, users need 
to have some experience with Python to use it effectively. 
However, to make the package more accessible to a wider range 
of users, `SysIdentPyGUI` was developed as a Graphical User 
Interface (GUI) for `SysIdentPy`. This allows any user to use 
`SysIdentPy's` outstanding functionalities without 
needing to write any line of code.

# Statement of need

`SysIdentPyGUI` is a web app for the Python module `SysIdentPy` in the format of a Graphical User Interface (GUI). It was written using the `Streamlit` library, which allows the creation of web apps in a compact Python syntax. `SysIdentPyGUI` was concepted as a alternative for people that would like to use `SysIdentPy` toolbox but aren't familiar with Python, such as medical or economy students. But even experienced users could take advantage of its facilities, for a quick and easy use of the system identification and simulation tools, through a cellphone for example. 

Besides this, there isn't any projects for NARX and NARMAX system identification in the shape of a GUI available, so its a relevant contribution to the field.

The application currently has the following `SysIdentPy` features implemented:

- NARX and NARMAX Model identification using four model structure selection algorithms (Acelerated orthogonal least squares, Forward regression least squares, Meta model structure selection and Entropic regression); two basis function (Polynomial and Fourier); a variety of estimator algorithms (such as least squares, recursive least squares and least mean squares); the capabilitie to identify SISO and MISO models and selecting the specific lag for each input and output; free run and k-steps ahead simulation; a intuitive list of regressors and its parameters; the results and residues plot; a complete list of metrics to analyze the model; possibility to download a model file for posterior usage.
- You are able to use the model file that was previously generated to analyze a new dataset and check metrics and plots as specified before.
- If the user has a known NARX model equation, the're able to input it on the web app and simulate the model with free run and k-steps ahead option and other parameters.

To use `SysIdentPyGUI` the user could access the app through the hosted server, cloning the repository or running a containerized version through Docker.

Further in this article is described examples of usage of the web app and future work, but more detailed information can also be found in the [documentation](https://jceneziojr.github.io/sysidentpygui/).

# Example of usage

## Model Identification

Through `SysIdentPyGUI`, with few clicks, you can quickly identify the mathematical model that approximates the behaviour of given data: first you upload your data, set the `Model Setup` parameters (or you could tweak through the default values until you obtain a decent predict) and finally you can analyze your results.

![Data loaded and validation percentage set](../paper/images/1.png)

![Model configuration parameters set](../paper/images/2.png)

![Predict results](../paper/images/3.png)

## Loading a model

If the user saved the model in their computer, they can load it and use other dataset to analyze the model fitting.

![Loading a previously fitted model](../paper/images/4.png)

## Simulate a Predefined Model

The user can simulate a NARX model known beforehand (regressors and parameters), using the regressors codification that is described in `SysIdentPy` documentation. Its as simple as loading the data, inputing the regressors list, setting the regressors parameters and configurating the simulation.

![Regressors code and parameters](../paper/images/5.png)

![Regressors code and parameters](../paper/images/6.png)

# Future Work

`SysIdentPyGUI` aims to be as self-maintaining as possible and up to date comparing to `SysIdentPy`. However, some features aren't available yet, like the Narx Neural Network. But they will be analyzed and deployed eventually, as well as the new features developed in the package.

# References