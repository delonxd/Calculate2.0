# from src.ParamType import ImpedanceType
import pickle


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


class TADXfmrParam(Parameter):
    """
        TAD变压器参数类
    """

    def __init__(self, name):
        super().__init__(name)
        self.z1 = None
        self.z2 = None
        self.n = None
        self.z3 = None
        self.zc = None

    @property
    def param_class(self):
        from src.Module.TcsrModule import TcsrTADXfmr
        return TcsrTADXfmr


class FLXfmrParam(Parameter):
    """
        防雷压器参数类
    """

    def __init__(self, name):
        super().__init__(name)
        self.z1 = None
        self.z2 = None
        self.n = None

    @property
    def param_class(self):
        from src.Module.TcsrModule import TcsrFLXfmr
        return TcsrFLXfmr


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

    @property
    def param_class(self):
        return

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

    @property
    def param_class(self):
        return

    def __setitem__(self, key, value):
        return self.dict.__setitem__(key, value)

    def __getitem__(self, item):
        return self.dict.__getitem__(item)