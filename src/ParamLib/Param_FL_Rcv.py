from src.Parameter import Parameter
from src.Parameter import FLXfmrParam
from src.ParamType import MultiFreqImpType
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = FLXfmrParam('Param_FL_Rcv')
    param_dict[param.name] = param

    param.z1 = MultiFreqImpType()
    param.z1.rlc_s = {
        1700: (5.5239, 513.56e-6, None),
        2000: (5.4992, 608.52e-6, None),
        2300: (5.5807, 705.17e-6, None),
        2600: (5.4392, 791.83e-6, None),
    }

    param.z2 = MultiFreqImpType()
    param.z2.rlc_p = {
        1700: (6.1620e3, 269.488e-3, None),
        2000: (6.8163e3, 279.317e-3, None),
        2300: (7.2892e3, 285.537e-3, None),
        2600: (8.0493e3, 296.218e-3, None),
    }

    param.n = {
        1700: 0.9690,
        2000: 0.9680,
        2300: 0.9719,
        2600: 0.9656,
    }

    Parameter.param_dict_to_pkl(param_dict)
    pass
