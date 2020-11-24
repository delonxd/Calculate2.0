from src.Parameter import Parameter
from src.ParamType import MultiFreqImpType
from src.Parameter import CableParam
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = MultiFreqImpType('Param_CA_QJ')
    param_dict[param.name] = param
    param.z_complex = {
        1700: (0.006459333 + 0.030996667j),
        2000: (0.007119667 + 0.035956660j),
        2300: (0.007735333 + 0.040813333j),
        2600: (0.008341333 + 0.045740000j),
    }

    param = MultiFreqImpType('Param_CA_ZN')
    param_dict[param.name] = param
    param.rlc_s = {
        1700: (10.35e-3, 4.68e-6, None),
        2000: (11.71e-3, 4.49e-6, None),
        2300: (13.01e-3, 4.40e-6, None),
        2600: (14.55e-3, 4.59e-6, None),
    }

    param = MultiFreqImpType('Param_SVA')
    param_dict[param.name] = param
    param.rlc_s = {
        1700: (15e-3, 33.001000e-6, None),
        2000: (17e-3, 32.897327e-6, None),
        2300: (20e-3, 32.800000e-6, None),
        2600: (22e-3, 32.700219e-6, None),
    }

    param = MultiFreqImpType('Param_SVA_Plus')
    param_dict[param.name] = param
    param.rlc_s = {
        1700: (37.95e-3, 31.55e-6, None),
        2000: (43.70e-3, 31.20e-6, None),
        2300: (45.60e-3, 31.00e-6, None),
        2600: (49.30e-3, 30.85e-6, None),
    }

    param = MultiFreqImpType('Param_Z_Rcv')
    param_dict[param.name] = param
    param.rlc_p = {
        1700: (23e3, 3.370340e-3, None),
        2000: (23e3, 3.366127e-3, None),
        2300: (23e3, 3.363013e-3, None),
        2600: (23e3, 3.366739e-3, None),
    }

    param = CableParam('Param_Cable')
    param_dict[param.name] = param
    param.R = 43
    param.L = 825e-6
    param.C = 28e-9

    Parameter.param_dict_to_pkl(param_dict)
    pass
