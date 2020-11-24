from src.Parameter import Parameter
from src.Parameter import ZPW2000AZPower
from src.ParamType import MultiFreqImpType
# import pickle


if __name__ == '__main__':
    param_dict = dict()

    param = ZPW2000AZPower('Param_Z_Power')
    param_dict[param.name] = param

    param[1] = MultiFreqImpType()
    param[1].z_complex = {
        1700: (22.30 + 29.00j),
        2000: (23.26 + 32.20j),
        2300: (23.93 + 36.77j),
        2600: (24.67 + 41.55j),
    }

    param[2] = MultiFreqImpType()
    param[2].z_complex = {
        1700: (18.60 + 21.50j),
        2000: (18.83 + 25.00),
        2300: (19.50 + 29.55j),
        2600: (19.80 + 31.85j),
    }

    param[3] = MultiFreqImpType()
    param[3].z_complex = {
        1700: (15.00 + 16.30j),
        2000: (15.20 + 18.50j),
        2300: (15.45 + 20.70j),
        2600: (15.90 + 23.90j),
    }

    param[4] = MultiFreqImpType()
    param[4].z_complex = {
        1700: (10.30 + 9.4j),
        2000: (11.00 + 11.0j),
        2300: (10.44 + 12.5j),
        2600: (11.00 + 14.0j),
    }

    param[5] = MultiFreqImpType()
    param[5].z_complex = {
        1700: (6.4 + 4.50j),
        2000: (6.4 + 5.16j),
        2300: (6.4 + 5.85j),
        2600: (6.4 + 6.52j),
    }

    param[6] = MultiFreqImpType()
    param[6].z_complex = {
        1700: (5.80 + 6.50j),
        2000: (5.70 + 7.55j),
        2300: (5.85 + 8.64j),
        2600: (6.00 + 9.65j),
    }

    param[7] = MultiFreqImpType()
    param[7].z_complex = {
        1700: (4.72 + 4.30j),
        2000: (4.77 + 5.05j),
        2300: (4.85 + 5.55j),
        2600: (4.93 + 6.23j),
    }

    param[8] = MultiFreqImpType()
    param[8].z_complex = {
        1700: (3.70 + 3.60j),
        2000: (3.76 + 4.18j),
        2300: (3.75 + 4.70j),
        2600: (3.86 + 5.23j),
    }

    param[9] = MultiFreqImpType()
    param[9].z_complex = {
        1700: (3.02 + 2.86j),
        2000: (3.09 + 3.30j),
        2300: (3.19 + 3.69j),
        2600: (3.21 + 4.10j),
    }

    Parameter.param_dict_to_pkl(param_dict)
    pass
