import numpy as np

basis_function_list = ['Polynomial', 'Fourier']
basis_function_parameter_list = [
    {   #polynomial
        'degree' : 2
    },
    {   #fourier
        'n' : 1,
        'p' : 2*np.pi,
        'degree' :  1,
        'ensemble' : True
    }
]

model_struc_dict = {
    'Forward regression orthogonal least squares' :  ['forward_regression_orthogonal_least_squares','FROLS'],
    'Accelerated orthogonal least squares' :  ['accelerated_orthogonal_least_squares','AOLS'],
    'Meta model structure selection' :  ['meta_model_structure_selection','MetaMSS'],
    'Entropic regression' :  ['entropic_regression','ER']
}
model_struc_selec_parameter_list = [
    {   #FROLS
        'ylag' :  2,
        'xlag' :  2,
        'elag' :  2,
        'order_selection' :  True, #MUDAR DEPOIS PRA FALSE
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
    {   #MetaMSS
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
        # 'loss_func' : "metamss_loss", #método da classe, mas tem o aic e bic
        'model_type' : "NARMAX",
        'basis_function' : None,
        # 'steps_ahead' : None, #não é o mesmo do predict
        # 'random_state' : None #int
    },
    {   #ER
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

estimators_list = ['least_squares', 'total_least_squares', 'recursive_least_squares', 'affine_least_mean_squares', 'least_mean_squares',
                    'least_mean_squares_sign_error', 'normalized_least_mean_squares', 'least_mean_squares_normalized_sign_error',
                    'least_mean_squares_sign_regressor', 'least_mean_squares_normalized_sign_regressor', 'least_mean_squares_sign_sign',
                    'least_mean_squares_normalized_sign_sign', 'least_mean_squares_normalized_leaky', 'least_mean_squares_leaky',
                    'least_mean_squares_fourth', 'least_mean_squares_mixed_norm']

model_type_list = ['NARMAX', 'NAR', 'NFIR']