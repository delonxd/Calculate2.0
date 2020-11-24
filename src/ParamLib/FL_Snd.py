from src.Parameter import Parameter
from src.Parameter import FLXfmrParam
from src.ParamType import MultiFreqImpType
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = FLXfmrParam('FL_Snd')
    param_dict[param.name] = param

    param.z1 = MultiFreqImpType()
    param.z1.rlc_s = {
        1700: (5.4106, 609.94e-6, None),
        2000: (5.5075, 732.70e-6, None),
        2300: (5.3495, 834.41e-6, None),
        2600: (5.4294, 949.34e-6, None),
    }

    param.z2 = MultiFreqImpType()
    param.z2.rlc_p = {
        1700: (12.7514e3, 2.314239, None),
        2000: (13.5088e3, 2.841193, None),
        2300: (12.7879e3, 2.597024, None),
        2600: (14.7951e3, 4.116232, None),
    }

    param.n = {
        1700: 0.9645,
        2000: 0.9695,
        2300: 0.9627,
        2600: 0.9668,
    }

    Parameter.param_dict_to_pkl(param_dict)
    pass
