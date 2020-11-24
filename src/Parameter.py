from src.ParamType import ImpedanceType


class Parameter:
    """
        标准参数类
    """

    from src.Module.TcsrModule import TcsrTADXfmr

    def __init__(self, name):
        self.name = name
        pass


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
