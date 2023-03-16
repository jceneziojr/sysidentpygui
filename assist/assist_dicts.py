import numpy as np
from sysidentpy.parameter_estimation import Estimators
import sysidentpy.basis_function as basis_function
import inspect
import assist.utils as utils

basis_function_list = [cls_name for cls_name,_ in inspect.getmembers(basis_function, lambda member: inspect.isclass(member))]
basis_function_parameter_list = [utils.get_default_args(getattr(basis_function, cls_name)) for cls_name in basis_function_list]

model_struc_dict = { #Nome que aparece, nome do arquivo, nome da classe
    'Forward regression orthogonal least squares (compact)' :  ['forward_regression_orthogonal_least_squares','FROLS'],
    'Forward regression orthogonal least squares (complete)' :  ['forward_regression_orthogonal_least_squares','FROLS'],
    'Accelerated orthogonal least squares' :  ['accelerated_orthogonal_least_squares','AOLS'],
    'Meta model structure selection (compact)' :  ['meta_model_structure_selection','MetaMSS'],
    'Meta model structure selection (complete)' :  ['meta_model_structure_selection','MetaMSS'],
    'Entropic regression (compact)' :  ['entropic_regression','ER'],
    'Entropic regression (complete)' :  ['entropic_regression','ER']
}
model_struc_selec_parameter_list = [
    { #FROLS compacto
        'order_selection' :  True, #o valor padrão é False, mas acho q faz mais sentido ser True aqui
        'n_terms' :  None,
        'n_info_values' : 10,
        'extended_least_squares' :  False,
        'ylag' :  2,
        'xlag' :  2,
        'info_criteria' :  "aic",
        'estimator' :  "recursive_least_squares",
        'model_type' :  "NARMAX",
        'basis_function' :  None
    },
    {   #FROLS completo
        'ylag' :  2,
        'xlag' :  2,
        'elag' :  2,
        'order_selection' :  True, 
        'info_criteria' :  "aic",
        'n_terms' :  None,
        'n_info_values' : 10,
        'estimator' :  "recursive_least_squares",
        'extended_least_squares' :  False,
        'lam' :  0.98,
        'delta' :  0.01,
        'offset_covariance' :  0.2,
        'mu' :  0.01,
        'eps' :  np.finfo(np.float64).eps,
        'gama' :  0.2,
        'weight' :  0.02,
        'basis_function' :  None,
        'model_type' :  "NARMAX"
    },
    {   #AOLS
        'ylag' : 2,
        'xlag' : 2,
        'k' : 1,
        'L' : 1,
        'threshold' : 10e-10,
        'model_type' : "NARMAX",
        'basis_function' : None
    },
    {   #MetaMSS compacto
        'maxiter' : 30,
        'k_agents_percent' : 2,
        'norm' : -2,
        'n_agents' : 10,
        'xlag' : 2,
        'ylag' : 2,
        'estimator' : "least_squares",
        'estimate_parameter' : True,
        'loss_func' : "metamss_loss",
        'model_type' : "NARMAX",
        'basis_function' : None
    },
    {   #MetaMSS completo
        'maxiter' : 30,
        'alpha' : 23,
        'g_zero' : 100,
        'k_agents_percent' : 2,
        'norm' : -2,
        'power' : 2,
        'n_agents' : 10,
        'p_zeros' : 0.5,
        'p_ones' : 0.5,
        'p_value' : 0.05,
        'xlag' : 2,
        'ylag' : 2,
        'elag' : 2,
        'estimator' : "least_squares",
        'extended_least_squares' : False,
        'lam' : 0.98,
        'delta' : 0.01,
        'offset_covariance' : 0.2,
        'mu' : 0.01,
        'eps' : np.finfo(np.float64).eps,
        'gama' : 0.2,
        'weight' : 0.02,
        'estimate_parameter' : True,
        'loss_func' : "metamss_loss",
        'model_type' : "NARMAX",
        'basis_function' : None,
        'steps_ahead' : None, #não é o mesmo do predict
        # 'random_state' : None #int
    },
    {   #ER compacto
        'ylag' : 2,
        'xlag' : 2,
        'estimator' : "least_squares",
        'k' : 2,
        'n_perm' : 200,
        'skip_forward' : False,
        'model_type' : "NARMAX",
        'basis_function' : None
    },
    {   #ER completo
        'ylag' : 2,
        'xlag' : 2,
        'q' : 0.99,
        'estimator' : "least_squares",
        'extended_least_squares' : False,
        'h' : 0.01,
        'k' : 2,
        # 'mutual_information_estimator' : "mutual_information_knn", #método da classe
        'n_perm' : 200,
        'p' : 1.797e307,
        'skip_forward' : False,
        'lam' : 0.98,
        'delta' : 0.01,
        'offset_covariance' : 0.2,
        'mu' : 0.01,
        'eps' : np.finfo(np.float64).eps,
        'gama' : 0.2,
        'weight' : 0.02,
        'model_type' : "NARMAX",
        'basis_function' : None,
        # 'random_state' : None
    }
]

ic_list = ["aic", "bic", "fpe", "lilc"]

estimators_list = utils.get_estimators(Estimators)

model_type_list = ['NARMAX', 'NAR', 'NFIR']

los_func_list = ['metamss_loss', 'aic', 'bic']