from src.Module.ElectricModule import PiCircuitModule


class TrackModule(PiCircuitModule):
    """
        钢轨模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = '钢轨模块'
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    def init_param(self, param_dict):
        self.load_kw(z=param_dict['Param_R_Track'])
