from src.Parameter import Parameter
from src.Parameter import TADXfmrParam
from src.ParamType import MultiFreqImpType
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = TADXfmrParam('TAD_Snd_ZN')
    param_dict[param.name] = param

    param.z1 = MultiFreqImpType()
    param.z1.rlc_s = {
        1700: (2.5082, 313.43e-6, None),
        2000: (2.5082, 313.43e-6, None),
        2300: (2.5082, 313.43e-6, None),
        2600: (2.5082, 313.43e-6, None),
    }

    param.z2 = MultiFreqImpType()
    param.z2.rlc_s = {
        1700: (2.5312e3, 0.284779, None),
        2000: (2.5312e3, 0.284779, None),
        2300: (2.5312e3, 0.284779, None),
        2600: (2.5312e3, 0.284779, None),
    }

    param.z3 = MultiFreqImpType()
    param.z3.rlc_s = {
        1700: (0.1, 4.2e-3, None),
        2000: (0.1, 4.2e-3, None),
        2300: (0.1, 4.2e-3, None),
        2600: (0.1, 4.2e-3, None),
    }

    param.zc = MultiFreqImpType()
    param.zc.rlc_s = {
        1700: (None, None, 2.35e-3),
        2000: (None, None, 2.35e-3),
        2300: (None, None, 2.35e-3),
        2600: (None, None, 2.35e-3),
    }

    param.n = {
        1700: 13.5,
        2000: 13.5,
        2300: 12,
        2600: 12,
    }

    Parameter.param_dict_to_pkl(param_dict)
    pass
