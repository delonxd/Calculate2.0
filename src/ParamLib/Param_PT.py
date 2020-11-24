from src.Parameter import Parameter
from src.Parameter import ZPW2000APTParam
from src.ParamType import MultiFreqImpType
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = ZPW2000APTParam('Param_PT')
    param_dict[param.name] = param

    param[1700] = MultiFreqImpType()
    param[1700].rlc_s = {
        1700: (7.02e-3, None, 261.48e-6),
        2000: (7.86e-3, None, 351.04e-6),
        2300: (11.63e-3, None, 2123e-6),
        2600: (85.9e-3, 50.823e-6, None),
    }

    param[2000] = MultiFreqImpType()
    param[2000].rlc_s = {
        1700: (8.01e-3, None, 159.403e-6),
        2000: (8.64e-3, None, 188.255e-6),
        2300: (10.0e-3, None, 268.51e-6),
        2600: (13.73e-3, None, 1362e-6),
    }

    param[2300] = MultiFreqImpType()
    param[2300].rlc_s = {
        1700: (23.54e-3, None, 2960e-6),
        2000: (1600e-3, 115.77e-6, None),
        2300: (39.51e-3, None, 141.889e-6),
        2600: (17.91e-3, None, 194.46e-6),
    }

    param[2600] = MultiFreqImpType()
    param[2600].rlc_s = {
        1700: (13.1e-3, None, 436.52e-6),
        2000: (25.69e-3, None, 2248.8e-6),
        2300: (1464.4e-3, 97.468e-6, None),
        2600: (48.82e-3, None, 112.316e-6),
    }

    Parameter.param_dict_to_pkl(param_dict)
    pass
