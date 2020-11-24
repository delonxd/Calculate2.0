# from src.ParamType import ImpedanceType
import pickle
import os


class Parameter:
    """
        标准参数类
    """

    def __init__(self, name):
        self.name = name
        pass

    @classmethod
    def param_dict_to_pkl(cls, param_dict):
        for param in param_dict.values():
            Parameter.param_to_pkl(param)

    @classmethod
    def param_to_pkl(cls, param):
        name = param.name
        address = '../ParamPkl/%s.pkl' % name
        with open(address, 'wb') as pk_f:
            pickle.dump(param, pk_f)

    # @classmethod
    # def read_param_lib(cls):
    #     dir_path = os.path.dirname(__file__)
    #     dir_path = os.path.join(dir_path, 'ParamLib')
    #     # print(dir_path)
    #     name_list = os.listdir(dir_path)
    #     for name in name_list:
    #         path = os.path.join(dir_path, name)
    #         os.system(path)
    #     tmp = Parameter.read_param_pkl()
    #     return tmp

    @classmethod
    def read_param_pkl(cls):
        param_dict = dict()
        dir_path = os.path.dirname(__file__)
        dir_path = os.path.join(dir_path, 'ParamPkl')
        # print(dir_path)
        name_list = os.listdir(dir_path)
        for name in name_list:
            path = os.path.join(dir_path, name)
            with open(path, 'rb') as pk_f:
                tmp = pickle.load(pk_f)
            param_dict[tmp.name] = tmp
        return param_dict


class TADXfmrParam(Parameter):
    """
        TAD变压器参数类
    """

    from src.Module.TcsrModule import TcsrTADXfmr
    param_class = TcsrTADXfmr

    def __init__(self, name):
        super().__init__(name)
        self.z1 = None
        self.z2 = None
        self.n = None
        self.z3 = None
        self.zc = None

    # @property
    # def param_class(self):
    #     from src.Module.TcsrModule import TcsrTADXfmr
    #     return TcsrTADXfmr


class FLXfmrParam(Parameter):
    """
        防雷压器参数类
    """

    def __init__(self, name):
        super().__init__(name)
        self.z1 = None
        self.z2 = None
        self.n = None


class FourFreqParam(Parameter):
    """
        4频率参数类
    """

    def __init__(self, name):
        super().__init__(name)
        self.dict = {
            1700: None,
            2000: None,
            2300: None,
            2600: None,
        }

    def __setitem__(self, key, value):
        return self.dict.__setitem__(key, value)

    def __getitem__(self, item):
        return self.dict.__getitem__(item)


class ZPW2000APTParam(FourFreqParam):
    """
        ZPW2000A PT参数类
    """


class ZPW2000ATBParam(FourFreqParam):
    """
        ZPW2000A TB参数类
    """


class ZPW2000AZPower(Parameter):
    """
        ZPW2000A 发送器内阻参数类
    """

    def __init__(self, name):
        super().__init__(name)
        self.dict = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }

    def __setitem__(self, key, value):
        return self.dict.__setitem__(key, value)

    def __getitem__(self, item):
        return self.dict.__getitem__(item)


class CableParam(Parameter):
    """
        TAD变压器参数类
    """

    def __init__(self, name):
        super().__init__(name)
        self.R = None
        self.L = None
        self.C = None
