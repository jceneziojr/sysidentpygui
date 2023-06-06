from sysidentpy.parameter_estimation import Estimators
import sysidentpy.basis_function as basis_function
import sysidentpy.model_structure_selection as model_structure_selection
import inspect
import assist.utils as utils

basis_function_list = [
    cls_name
    for cls_name, _ in inspect.getmembers(
        basis_function, lambda member: inspect.isclass(member)
    )
]

basis_function_parameter_list = [
    utils.get_default_args(getattr(basis_function, cls_name))
    for cls_name in basis_function_list
]

model_struc_dict = utils.get_model_struc_dict(
    model_structure_selection, "sysidentpy.model_structure_selection."
)

model_struc_selec_parameter_list = utils.get_model_struc_selec_parameter_list(
    model_structure_selection
)

estimators_list = utils.get_estimators(Estimators)

ic_list = ["aic", "bic", "fpe", "lilc"]

model_type_list = ["NARMAX", "NAR", "NFIR"]

los_func_list = ["metamss_loss", "aic", "bic"]
