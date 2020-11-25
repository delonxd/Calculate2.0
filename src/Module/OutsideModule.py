from src.Module.ElectricModule import ImpedanceModule


class ZPW2000A_SVA(ImpedanceModule):
    """
        SVA模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = 'ZPW2000A空心线圈模块'
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    def init_param(self, param_dict):
        self.load_kw(z=param_dict['Param_SVA'])


class ZPW2000A_CapC(ImpedanceModule):
    """
        补偿电容模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = 'ZPW2000A电容模块'
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    def init_param(self, param_dict):
        self.load_kw(z=param_dict['Param_CapC'])


class ZPW2000A_TB(ImpedanceModule):
    """
        TB模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = 'ZPW2000A_TB模块'
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    @property
    def z(self):
        return self.param[0][self.main_freq]

    @property
    def main_freq(self):
        return self.parent.freq

    def init_param(self, param_dict):
        self.load_kw(z=param_dict['Param_TB'])


class Outside_R_Short(ImpedanceModule):
    """
        分路阻抗模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = '分路电阻'
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    def init_param(self, param_dict):
        self.load_kw(z=param_dict['Param_R_Short'])
