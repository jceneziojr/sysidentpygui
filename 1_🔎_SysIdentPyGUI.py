# os comentários não são feitos do modo usual (usando as aspas e varias linhas), pois o streamlit interpreta o texto solto no código
# entre aspas como string, e 'printa' o texto na aplicação

import streamlit as st
import os
import pandas as pd
from assist.assist_dicts import (
    basis_function_list,
    basis_function_parameter_list,
    model_struc_dict,
    model_struc_selec_parameter_list,
    ic_list,
    estimators_list,
    model_type_list,
    los_func_list,
)
import assist.utils as utils
import importlib
from sysidentpy.basis_function import *
from sysidentpy.model_structure_selection import *
from sysidentpy.metrics import __ALL__ as metrics_list
import sysidentpy.metrics as metrics
from sysidentpy.utils.display_results import results
from sysidentpy.residues.residues_correlation import (
    compute_residues_autocorrelation,
    compute_cross_correlation,
)
import pickle as pk
from math import floor
import platform

if platform.system() == "Linux":
    root = os.path.join(os.path.dirname(__file__) + "/assist")
else:
    root = os.path.join(os.path.dirname(__file__) + "\\assist")
path = os.path.join(root, "pagedesign.py")

with open(path, encoding="utf-8") as code:
    c = code.read()
    exec(c, globals())

tabl = ["Load Data", "Model Setup", "Model Validation and Metrics", "Save Model"]

tab1, tab2, tab3, tab4 = st.tabs(tabl)

with tab1:
    col, esp0, col0 = st.columns([5, 1, 5])

    with col:
        st.file_uploader("Input Data", key="x_data", help="Upload your CSV file")
        if st.session_state["x_data"] != None:
            data_x = pd.read_csv(st.session_state["x_data"], sep="\t")

    with col0:
        st.file_uploader("Output Data", key="y_data", help="Upload your CSV file")
        if st.session_state["y_data"] != None:
            data_y = pd.read_csv(st.session_state["y_data"], sep="\t")

    col1, esp1, esp2 = st.columns([2, 1, 7])  # ajustando a largura dos widgets
    with col1:
        st.number_input("Validating Percentage", 0.0, 100.0, value=15.0, key="val_perc")
    st.markdown("""---""")
    with st.expander("Instructions"):
        st.write(
            "Load above your .csv/.txt input and output data, formatted in a column (in case of multiple inputs, use a tab as a separator). Then, set the percentage of the data that will be used as validation data."
        )
        st.write(
            "For better performance, load your output data after setting up your model. The input data is required so the app can identify the number of inputs (therefore, the user cannot setup the model without loading the input data)."
        )
        st.write(
            "You can download the model once both the input and output data have been loaded."
        )
        st.write(
            "We are aware of a bug that happens when you change the Model Structure Selection Algorithm. If you press the 'R' key it will solve it. The cause of the bug is known, but a fix is not really doable within our code format."
        )

    if st.session_state["x_data"] != None:  # não é o melhor jeito de fazer isso
        perc_index = floor(
            data_x.shape[0] - data_x.shape[0] * (st.session_state["val_perc"] / 100)
        )
        x_train, x_valid = (
            data_x[0:perc_index].to_numpy(),
            data_x[perc_index:].to_numpy(),
        )  # o formato padrão é ndarray

    if st.session_state["y_data"] != None:  # não é o melhor jeito de fazer isso
        perc_index = floor(
            data_x.shape[0] - data_x.shape[0] * (st.session_state["val_perc"] / 100)
        )
        y_train, y_valid = (
            data_y[0:perc_index].to_numpy(),
            data_y[perc_index:].to_numpy(),
        )
with tab2:
    if st.session_state["x_data"] != None:
        col2, esp3, esp4 = st.columns([2, 1, 1.65])
        with col2:
            st.selectbox(
                "Basis Function", basis_function_list, key="basis_function_key", index=1
            )  # escolhendo a basis function

            for i in range(
                len(basis_function_list)
            ):  # pra saber quantos widgets devem ser criados, é preciso que a gente saiba qual basis function foi escolhida,
                # então a variável i serve pra checarmos isso

                if (
                    st.session_state["basis_function_key"] == basis_function_list[i]
                ):  # se a basis function escolhida for a mesma da iteração atual, segundo i, roda o código
                    # criando os widgets
                    wcont1 = (
                        0  # variável de assistência pra criar os widgets recursivamente
                    )
                    key_list = list(
                        basis_function_parameter_list[i]
                    )  # essa lista das keys do dict de parametros, serve para acessar os values e ser a label dos widgets
                    while wcont1 < len(
                        utils.dict_values_to_list(basis_function_parameter_list[i])
                    ):  # criando os widgets recursivamente, e atribuindo os nomes p/ os widgets
                        k = "bf_par_" + str(wcont1)

                        if isinstance(
                            basis_function_parameter_list[i][key_list[wcont1]], int
                        ):
                            if isinstance(
                                basis_function_parameter_list[i][key_list[wcont1]], bool
                            ):
                                st.write(utils.adjust_string(key_list[wcont1]))
                                st.checkbox(
                                    "",
                                    key=k,
                                    value=basis_function_parameter_list[i][
                                        key_list[wcont1]
                                    ],
                                )  # no checkbox, a label é automaticamente a direita, então
                                # chamo antes em cima
                            else:
                                st.number_input(
                                    utils.adjust_string(key_list[wcont1]),
                                    key=k,
                                    min_value=0,
                                    value=basis_function_parameter_list[i][
                                        key_list[wcont1]
                                    ],
                                )

                        if isinstance(
                            basis_function_parameter_list[i][key_list[wcont1]], float
                        ):
                            st.number_input(
                                utils.adjust_string(key_list[wcont1]),
                                key=k,
                                min_value=0.0,
                                value=basis_function_parameter_list[i][
                                    key_list[wcont1]
                                ],
                                format="%5.3e",
                                step=basis_function_parameter_list[i][key_list[wcont1]]
                                / 10,
                            )

                        if isinstance(
                            basis_function_parameter_list[i][key_list[wcont1]], str
                        ):
                            st.write("string")

                        wcont1 = wcont1 + 1

                    bf_par_dict = dict(
                        basis_function_parameter_list[i]
                    )  # aqui ele copia o dicionario base dos parametros, para assim substituir com os valores novos
                    # obtidos no widget
                    bf_par_list = (
                        list()
                    )  # lista p/ pegar as keys dos widgets e podermos atribuir os valores corretos ao dict acima

                    if utils.occurrence_check("bf_par_", list(st.session_state)) != len(
                        utils.dict_values_to_list(basis_function_parameter_list[i])
                    ):
                        # quando troca de basis function, se o numero de parametros é menor, dá um erro porque tem keys a mais de session state
                        # aqui, apago os excedentes
                        for key in utils.session_state_cut(
                            st.session_state,
                            "bf_par_",
                            len(
                                utils.dict_values_to_list(
                                    basis_function_parameter_list[i]
                                )
                            ),
                        ):
                            del st.session_state[key]

                    for j in range(
                        len(list(st.session_state))
                    ):  # pegando as keys de session state que tem o nome base para ser widget dos parametros de basis function
                        if list(st.session_state)[j].startswith("bf_par_"):
                            bf_par_list.append(list(st.session_state)[j])

                    bf_par_list = sorted(
                        bf_par_list
                    )  # a lista precisa estar em ordem alfabética para o próximo bloco

                    for j in range(
                        len(bf_par_list)
                    ):  # refazendo o dicionário para os argumentos do objeto da basis function
                        bf_par_dict[
                            list(basis_function_parameter_list[i])[j]
                        ] = st.session_state[bf_par_list[j]]
        st.markdown("""---""")

        bf_module = importlib.import_module(
            "sysidentpy.basis_function._basis_function"
        )  # pegando o arquivo onde tá a classe da basis function
        bf = utils.str_to_class(st.session_state["basis_function_key"], bf_module)(
            **bf_par_dict
        )  # instanciando a basis function

        col3, esp5, esp6 = st.columns([3, 1, 1])
        with col3:
            st.selectbox(
                "Model Structure Selection Algorithm",
                list(model_struc_dict),
                key="model_struc_select_key",
                index=3,
            )

        col4, esp7, esp8 = st.columns([3, 1, 2.2])
        with col4:
            for i in range(len(model_struc_dict)):
                if (
                    st.session_state["model_struc_select_key"]
                    == list(model_struc_dict)[i]
                ):
                    wcont2 = 0
                    key_list = list(model_struc_selec_parameter_list[i])
                    while wcont2 < len(
                        utils.dict_values_to_list(model_struc_selec_parameter_list[i])
                    ):
                        k = "mss_par_" + str(wcont2)
                        if isinstance(
                            model_struc_selec_parameter_list[i][key_list[wcont2]], int
                        ):
                            if isinstance(
                                model_struc_selec_parameter_list[i][key_list[wcont2]],
                                bool,
                            ):
                                st.write(utils.adjust_string(key_list[wcont2]))
                                st.checkbox(
                                    "",
                                    key=k,
                                    value=model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ],
                                )
                            else:
                                if (
                                    model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ]
                                    < 0
                                ):
                                    st.number_input(
                                        utils.adjust_string(key_list[wcont2]),
                                        key=k,
                                        min_value=-50,
                                        value=model_struc_selec_parameter_list[i][
                                            key_list[wcont2]
                                        ],
                                    )
                                else:
                                    if key_list[wcont2] == "xlag":
                                        if x_train.shape[1] == 1:
                                            st.number_input(
                                                utils.adjust_string(key_list[wcont2]),
                                                key="x_lag",
                                                min_value=1,
                                                value=model_struc_selec_parameter_list[
                                                    i
                                                ][key_list[wcont2]],
                                            )
                                            st.multiselect(
                                                "Select the desired lags",
                                                utils.get_lags_list(
                                                    st.session_state["x_lag"]
                                                ),
                                                default=utils.get_lags_list(
                                                    st.session_state["x_lag"]
                                                ),
                                                key=k,
                                            )
                                        else:
                                            st.session_state[k] = list()
                                            for n_inputs in range(x_train.shape[1]):
                                                st.number_input(
                                                    utils.adjust_string(
                                                        key_list[wcont2]
                                                    )
                                                    + " "
                                                    + str(n_inputs + 1),
                                                    key="x_lag_" + str(n_inputs + 1),
                                                    min_value=1,
                                                    value=model_struc_selec_parameter_list[
                                                        i
                                                    ][
                                                        key_list[wcont2]
                                                    ],
                                                )
                                                st.multiselect(
                                                    "Select the desired lags",
                                                    utils.get_lags_list(
                                                        st.session_state[
                                                            "x_lag_" + str(n_inputs + 1)
                                                        ]
                                                    ),
                                                    default=utils.get_lags_list(
                                                        st.session_state[
                                                            "x_lag_" + str(n_inputs + 1)
                                                        ]
                                                    ),
                                                    key="lags_" + str(n_inputs + 1),
                                                )
                                                st.session_state[k].append(
                                                    st.session_state[
                                                        "lags_" + str(n_inputs + 1)
                                                    ]
                                                )
                                    else:
                                        if key_list[wcont2] == "ylag":
                                            st.number_input(
                                                utils.adjust_string(key_list[wcont2]),
                                                key="y_lag",
                                                min_value=1,
                                                value=model_struc_selec_parameter_list[
                                                    i
                                                ][key_list[wcont2]],
                                            )
                                            st.multiselect(
                                                "Select the desired lags",
                                                utils.get_lags_list(
                                                    st.session_state["y_lag"]
                                                ),
                                                default=utils.get_lags_list(
                                                    st.session_state["y_lag"]
                                                ),
                                                key=k,
                                            )
                                        else:
                                            st.number_input(
                                                utils.adjust_string(key_list[wcont2]),
                                                key=k,
                                                min_value=0,
                                                value=model_struc_selec_parameter_list[
                                                    i
                                                ][key_list[wcont2]],
                                            )

                        if (
                            model_struc_selec_parameter_list[i][key_list[wcont2]]
                            is None
                        ):
                            if (
                                key_list[wcont2] == "basis_function"
                            ):  # a basis function é escolhida antes, então não precisamos do widget aqui
                                pass
                            elif key_list[wcont2] == "n_terms":
                                if k not in st.session_state:
                                    st.session_state[
                                        k
                                    ] = model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ]
                                if "n_terms" in st.session_state:
                                    st.session_state[k] = st.session_state["n_terms"]
                            elif key_list[wcont2] == "steps_ahead":
                                if k not in st.session_state:
                                    st.session_state[
                                        k
                                    ] = model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ]
                                if "steps_aheadmss" in st.session_state:
                                    st.session_state[k] = st.session_state[
                                        "steps_aheadmss"
                                    ]
                                st.write(utils.adjust_string(key_list[wcont2]))
                                st.checkbox(" ", key="sa_c")
                            elif key_list[wcont2] == "random_state":
                                if k not in st.session_state:
                                    st.session_state[
                                        k
                                    ] = model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ]
                                if "random_statemss" in st.session_state:
                                    st.session_state[k] = st.session_state[
                                        "random_statemss"
                                    ]
                                st.write(utils.adjust_string(key_list[wcont2]))
                                st.checkbox(" ", key="rs_c")
                            else:
                                st.write(key_list[wcont2])
                                if st.checkbox(""):
                                    st.write("")
                                st.write("None Type here")

                        if isinstance(
                            model_struc_selec_parameter_list[i][key_list[wcont2]], float
                        ):
                            if (
                                model_struc_selec_parameter_list[i][key_list[wcont2]]
                                < 0.0
                            ):
                                st.number_input(
                                    utils.adjust_string(key_list[wcont2]),
                                    key=k,
                                    min_value=-50.0,
                                    value=model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ],
                                    format="%5.3e",
                                    step=model_struc_selec_parameter_list[i][
                                        key_list[wcont2]
                                    ]
                                    / 10,
                                )
                            else:
                                if key_list[wcont2] == "p":
                                    st.number_input(
                                        utils.adjust_string(key_list[wcont2]),
                                        key=k,
                                        min_value=0.0,
                                        value=1.797e307,
                                        format="%5.3e",
                                        step=1.797e307 / 10,
                                    )
                                else:
                                    st.number_input(
                                        utils.adjust_string(key_list[wcont2]),
                                        key=k,
                                        min_value=0.0,
                                        value=model_struc_selec_parameter_list[i][
                                            key_list[wcont2]
                                        ],
                                        format="%5.3e",
                                        step=0.5,
                                    )

                        if isinstance(
                            model_struc_selec_parameter_list[i][key_list[wcont2]], str
                        ):  # os valores padrão não vem do dicionário externo, porque o valor padrão é o primeiro elemento da lista que passamos como opções
                            if key_list[wcont2] == "info_criteria":
                                st.selectbox(
                                    utils.adjust_string(key_list[wcont2]),
                                    ic_list,
                                    key=k,
                                )
                            if key_list[wcont2] == "estimator":
                                st.selectbox(
                                    utils.adjust_string(key_list[wcont2]),
                                    estimators_list,
                                    key=k,
                                )
                            if key_list[wcont2] == "model_type":
                                st.selectbox(
                                    utils.adjust_string(key_list[wcont2]),
                                    model_type_list,
                                    key=k,
                                )
                            if key_list[wcont2] == "loss_func":
                                st.selectbox(
                                    utils.adjust_string(key_list[wcont2]),
                                    los_func_list,
                                    key=k,
                                )
                            if key_list[wcont2] == "mutual_information_estimator":
                                st.selectbox(
                                    utils.adjust_string(key_list[wcont2]),
                                    ["mutual_information_knn"],
                                    key=k,
                                )

                        if (
                            key_list[wcont2] == "order_selection"
                        ):  # se esse parametro for falso, um n_terms tem que ser escolhido
                            if st.session_state[k] == False:
                                st.number_input(
                                    utils.adjust_string("n_terms"),
                                    key="n_terms",
                                    min_value=1,
                                )
                            else:
                                st.session_state[
                                    "n_terms"
                                ] = model_struc_selec_parameter_list[i]["n_terms"]

                        if key_list[wcont2] == "steps_ahead":
                            if st.session_state["sa_c"] == True:
                                st.number_input(" ", key="steps_aheadmss", min_value=1)
                            else:
                                st.session_state[
                                    "steps_aheadmss"
                                ] = model_struc_selec_parameter_list[i]["steps_ahead"]
                        if key_list[wcont2] == "random_state":
                            if st.session_state["rs_c"] == True:
                                st.number_input(" ", key="random_statemss", min_value=1)
                            else:
                                st.session_state[
                                    "random_statemss"
                                ] = model_struc_selec_parameter_list[i]["random_state"]

                        wcont2 = wcont2 + 1

                    model_struc_selec_par_dict = dict(
                        model_struc_selec_parameter_list[i]
                    )
                    model_struc_selec_par_list = list()

                    if utils.occurrence_check(
                        "mss_par_", list(st.session_state)
                    ) != len(
                        utils.dict_values_to_list(model_struc_selec_parameter_list[i])
                    ):
                        # quando troca de basis function, se o numero de parametros é menor, dá um erro porque tem keys a mais de session state
                        # aqui, apago os excedentes
                        for key in utils.session_state_cut(
                            st.session_state,
                            "mss_par_",
                            len(
                                utils.dict_values_to_list(
                                    model_struc_selec_parameter_list[i]
                                )
                            ),
                        ):
                            del st.session_state[key]

                    for j in range(len(list(st.session_state))):
                        if list(st.session_state)[j].startswith("mss_par_"):
                            model_struc_selec_par_list.append(list(st.session_state)[j])
                    model_struc_selec_par_list = utils.sorter(
                        model_struc_selec_par_list
                    )

                    for j in range(len(model_struc_selec_par_list)):
                        model_struc_selec_par_dict[
                            list(model_struc_selec_parameter_list[i])[j]
                        ] = st.session_state[model_struc_selec_par_list[j]]
                    model_struc_selec_par_dict["basis_function"] = bf
                    if "n_terms" in model_struc_selec_parameter_list[i]:
                        model_struc_selec_par_dict["n_terms"] = st.session_state[
                            "n_terms"
                        ]
                    if "steps_ahead" in model_struc_selec_parameter_list[i]:
                        model_struc_selec_par_dict["steps_ahead"] = st.session_state[
                            "steps_aheadmss"
                        ]
                    if "random_state" in model_struc_selec_parameter_list[i]:
                        model_struc_selec_par_dict["random_state"] = st.session_state[
                            "random_statemss"
                        ]

        st.markdown("""---""")

        model_struc_selec_module = importlib.import_module(
            "sysidentpy.model_structure_selection"
            + "."
            + model_struc_dict[st.session_state["model_struc_select_key"]][0]
        )
        model = utils.str_to_class(
            model_struc_dict[st.session_state["model_struc_select_key"]][1],
            model_struc_selec_module,
        )(**model_struc_selec_par_dict)

    if (
        st.session_state["y_data"] != None and st.session_state["x_data"] != None
    ):  # não é o melhor jeito de fazer isso
        st.write("Predict Options")
        if isinstance(model, MetaMSS):  # MetaMSS tem métodos diferentes
            model.fit(X_train=x_train, y_train=y_train, X_test=x_valid, y_test=y_valid)
            if "steps_ahead" not in st.session_state:
                st.session_state["steps_ahead"] = None
            if "forecast_horizon" not in st.session_state:
                st.session_state["forecast_horizon"] = None
            st.write("Free Run Simulation")
            if st.checkbox("", value=True, key="free_run") is False:
                st.number_input("Steps Ahead", key="steps_ahead", min_value=1)
                if model.model_type == "NAR":
                    st.number_input(
                        "Forecast Horizon", key="forecast_horizon", min_value=1
                    )
            yhat = model.predict(
                X_test=x_valid,
                y_test=y_valid,
                steps_ahead=st.session_state["steps_ahead"],
                forecast_horizon=st.session_state["forecast_horizon"],
            )

        else:
            model.fit(X=x_train, y=y_train)
            if "steps_ahead" not in st.session_state:
                st.session_state["steps_ahead"] = None
            if "forecast_horizon" not in st.session_state:
                st.session_state["forecast_horizon"] = None
            st.write("Free Run Simulation")
            if st.checkbox("", value=True, key="free_run") is False:
                st.number_input("Steps Ahead", key="steps_ahead", min_value=1)
                if model.model_type == "NAR":
                    st.number_input(
                        "Forecast Horizon", key="forecast_horizon", min_value=1
                    )
            yhat = model.predict(
                X=x_valid,
                y=y_valid,
                steps_ahead=st.session_state["steps_ahead"],
                forecast_horizon=st.session_state["forecast_horizon"],
            )

with tab3:
    if (
        st.session_state["y_data"] != None and st.session_state["x_data"] != None
    ):  # não é o melhor jeito de fazer isso
        st.write("Model Regressors")
        r = pd.DataFrame(
            results(
                model.final_model,
                model.theta,
                model.err,
                model.n_terms,
                err_precision=8,
                dtype="sci",
            ),
            columns=["Regressors", "Parameters", "ERR"],
        )
        st.dataframe(r)

        ee = compute_residues_autocorrelation(y_valid, yhat)
        if x_train.shape[1] == 1:
            x1e = compute_cross_correlation(y_valid, yhat, x_valid)
        else:
            x1e = compute_cross_correlation(y_valid, yhat, x_valid[:, 0])
        with st.expander("Results Plot"):
            if st.session_state["free_run"] == True:
                st.image(utils.plot_results(y=y_valid, yhat=yhat, n=1000))
            else:
                st.image(
                    utils.plot_results(
                        y=y_valid,
                        yhat=yhat,
                        n=1000,
                        title=str(st.session_state["steps_ahead"])
                        + " Steps ahead simulation",
                    )
                )
        with st.expander("Residues Plot"):
            st.image(
                utils.plot_residues_correlation(
                    data=ee, title="Residues", ylabel="$e^2$"
                )
            )
            st.image(
                utils.plot_residues_correlation(
                    data=x1e, title="Residues", ylabel="$x_1e$", second_fig=True
                )
            )

        metrics_df = dict()
        metrics_namelist = list()
        metrics_vallist = list()  # criando listas separadas deixa mais bonito
        with st.expander("Metrics"):
            for index in range(len(metrics_list)):
                if (
                    metrics_list[index] == "r2_score"
                    or metrics_list[index] == "forecast_error"
                ):
                    pass
                else:
                    metrics_namelist.append(
                        utils.get_acronym(utils.adjust_string(metrics_list[index]))
                    )
                    metrics_vallist.append(
                        getattr(metrics, metrics_list[index])(y_valid, yhat)
                    )
            metrics_df["Metric Name"] = metrics_namelist
            metrics_df["Value"] = metrics_vallist
            st.dataframe(pd.DataFrame(metrics_df).style.format({"Value": "{:f}"}))

with tab4:
    # ''' [![Repo](https://badgen.net/github/release/wilsonrljr/sysidentpy/?icon=github&labelColor=373736&label&color=f47c1c)](https://github.com/wilsonrljr/sysidentpy) '''

    if st.session_state["y_data"] != None and st.session_state["x_data"] != None:
        st.download_button(
            "Download Model",
            data=pk.dumps(model),
            file_name="my_model.syspy",
        )
