from src.Module.ElectricModule import PiCircuitModule
import numpy as np


class TrackModule(PiCircuitModule):
    """
        钢轨模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = '钢轨模块'
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):
        if 'z_trk' in kwargs:
            self._param[0] = kwargs['z_trk']

        if 'rd' in kwargs:
            self._param[1] = kwargs['rd']

        if 'length' in kwargs:
            self._param[2] = kwargs['length']

    @property
    def z_trk(self):
        return self.param[0]

    @property
    def rd(self):
        return self.param[1]

    @property
    def length(self):
        return self.parent.length

    def config_param(self, freq):
        z_trk = self.z_trk
        rd = self.rd.z(freq)
        length = self.length / 1000
        if length == np.inf:
            zii = np.inf
            z_rd = np.inf
        else:
            z0 = z_trk.z(freq)
            y0 = 1 / rd
            zc = np.sqrt(z0 / y0)
            gama = np.sqrt(z0 * y0)
            zii = zc * np.sinh(gama * length)
            yii = (np.cosh(gama * length) - 1) / zc / np.sinh(gama * length)
            # rii = np.real(1 / yii)
            # yii = 1 / rii
            # y_tk = 1 / zii
            # y_rd = yii
            z_rd = 1 / yii

        self.r1.config_param(z_rd)
        self.r2.config_param(zii)
        self.r3.config_param(z_rd)

    def init_param(self, param_dict):
        self.load_kw(z_trk=param_dict['Param_Z_Track'])
        self.load_kw(rd=param_dict['Param_Rd'])

