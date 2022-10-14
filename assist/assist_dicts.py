import numpy as np

bas_fun_list = ['Polynomial', 'Fourier']
par_list = [
    {   #polynomial
        'degree' : 2
    },
    {   #fourier
        'n' : 1,
        'p' : 2*np.pi,
        'degree': 1,
        'ensemble' : True
    }
]
model_struc_dict = {
    'Forward regression orthogonal least squares': ['forward_regression_orthogonal_least_squares','FROLS'],
    'Accelerated orthogonal least squares': ['accelerated_orthogonal_least_squares','AOLS'],
    'Meta model structure selection': ['meta_model_structure_selection','MetaMSS'],
    'Entropic regression': ['entropic_regression','ER']
}

