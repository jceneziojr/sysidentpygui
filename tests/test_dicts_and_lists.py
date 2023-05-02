from sysidentpy.parameter_estimation import Estimators
import sysidentpy.basis_function as basis_function
import sysidentpy.model_structure_selection as model_structure_selection
import inspect
import platform
import os
import sys

if platform.system() == "Linux":
    sys.path.append(os.path.join(os.path.dirname(__file__).replace('/tests','')+'/assist'))
else:
    sys.path.append(os.path.join(os.path.dirname(__file__).replace('\\tests','')+'\\assist'))

import utils

class TestDictsAndLists():
    """
    Class for testing the proper creation of the necessary
    dictionarys and lists
    """
    def generate_basis_function_list(self):
        try:
            basis_function_list = [cls_name for cls_name,_ in inspect.getmembers(basis_function, lambda member: inspect.isclass(member))]
        except:
            return False
        else:
            return True
        
    def generate_basis_function_parameter_list(self):
        try:
            basis_function_list = [cls_name for cls_name,_ in inspect.getmembers(basis_function, lambda member: inspect.isclass(member))]
            basis_function_parameter_list = [utils.get_default_args(getattr(basis_function, cls_name)) for cls_name in basis_function_list]
        except:
            return False
        else:
            return True
    
    def generate_model_struc_dict(self):
        try:
            model_struc_dict = utils.get_model_struc_dict(model_structure_selection, 'sysidentpy.model_structure_selection.')      
        except:
            return False
        else:
            return True
        
    def generate_model_struc_selec_parameter_list(self):
        try:
            model_struc_selec_parameter_list = utils.get_model_struc_selec_parameter_list(model_structure_selection)
        except:
            return False
        else:
            return True
        
    def generate_estimators_list(self):
        try:
            estimators_list = utils.get_estimators(Estimators)
        except:
            return False
        else:
            return True        

    def test_basis_function_list(self):
        assert self.generate_basis_function_list() == True

    def test_basis_function_parameter_list(self):
        assert self.generate_basis_function_parameter_list() == True

    def test_model_struc_dict(self):
        assert self.generate_model_struc_dict() == True

    def test_model_struc_selec_parameter_list(self):
        assert self.generate_model_struc_selec_parameter_list() == True

    def test_estimators_list(self):
        assert self.generate_estimators_list() == True