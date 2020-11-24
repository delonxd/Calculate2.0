from src.Parameter import Parameter
from src.Parameter import TADXfmrParam
from src.ParamType import MultiFreqImpType
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = TADXfmrParam('Param_TAD_Snd_QJ')
    param_dict[param.name] = param

    param.z1 = MultiFreqImpType()
    param.z1.rlc_s = {
        1700: (3.9146, 581.14e-6, None),
        2000: (3.9695, 684.89e-6, None),
        2300: (3.8636, 769.06e-6, None),
        2600: (3.7937, 959.15e-6, None),
    }

    param.z2 = MultiFreqImpType()
    param.z2.rlc_p = {
        1700: (3.0451e3, 551.191e-3, None),
        2000: (3.1163e3, 580.653e-3, None),
        2300: (3.1775e3, 605.011e-3, None),
        2600: (3.2591e3, 635.065e-3, None),
    }

    param.z3 = MultiFreqImpType()
    param.z3.rlc_s = {
        1700: (250e-3, 4.2e-3, None),
        2000: (250e-3, 4.2e-3, None),
        2300: (250e-3, 4.2e-3, None),
        2600: (250e-3, 4.2e-3, None),
    }

    param.zc = MultiFreqImpType()
    param.zc.rlc_s = {
        1700: (None, None, 4.7e-3),
        2000: (None, None, 4.7e-3),
        2300: (None, None, 4.7e-3),
        2600: (None, None, 4.7e-3),
    }

    param.n = {
        1700: 8.9202,
        2000: 8.8912,
        2300: 8.8508,
        2600: 8.8688,
    }

    Parameter.param_dict_to_pkl(param_dict)
    pass
