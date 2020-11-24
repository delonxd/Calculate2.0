from src.Module.ElectricModule import ImpedanceModule
from src.Module.BasicModule import BasicModule
from src.Module.TcsrModule import TcsrPower
from src.Module.TcsrModule import TcsrReceiver
from src.Module.TcsrModule import TcsrFLXfmr
from src.Module.ElectricModule import CableModule
from src.Module.TcsrModule import TcsrTADXfmr
from src.Module.TcsrModule import TcsrBA
from src.Module.TcsrModule import TcsrCA


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


class ZPW2000A_TCSR_QJ_Normal(BasicModule):
    """
        2000A区间模块
    """

    def __init__(self, parent, **kwargs):
        from src.Unit.TcsrUnit import Snd_Mde, Rcv_Mde
        bas_name = 'ZPW2000A区间模块'
        super().__init__(parent, bas_name)
        # self.parameter = None

        self.power = TcsrPower(self, '1发送器')
        self.receiver = TcsrReceiver(self, '1接收器')
        self.fl_xfmr = TcsrFLXfmr(self, '2FL')
        self.cable = CableModule(self, '3电缆')
        self.tad_xfmr = TcsrTADXfmr(self, '4TAD')
        self.ba = TcsrBA(self, '5PT')
        self.ca = TcsrCA(self, '6CA')

        if parent.mode == Snd_Mde:
            self.add_element(self.power)
        elif parent.mode == Rcv_Mde:
            self.add_element(self.receiver)
        self.add_element(self.fl_xfmr)
        self.add_element(self.cable)
        self.add_element(self.tad_xfmr)
        self.add_element(self.ba)
        self.add_element(self.ca)

        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):

        if 'z_pwr' in kwargs:
            self.power.load_kw(z_pwr=kwargs['z_pwr'])

        if 'u_pwr' in kwargs:
            self.power.load_kw(z_pwr=kwargs['u_pwr'])

        if 'z_rcv' in kwargs:
            self.receiver.load_kw(z=kwargs['z_rcv'])

        if 'fl_z1' in kwargs:
            self.fl_xfmr.load_kw(z1=kwargs['fl_z1'])

        if 'fl_z2' in kwargs:
            self.fl_xfmr.load_kw(z2=kwargs['fl_z2'])

        if 'fl_n' in kwargs:
            self.fl_xfmr.load_kw(n=kwargs['fl_n'])

        if 'cb_r' in kwargs:
            self.cable.load_kw(R=kwargs['cb_r'])

        if 'cb_l' in kwargs:
            self.cable.load_kw(L=kwargs['cb_l'])

        if 'cb_c' in kwargs:
            self.cable.load_kw(C=kwargs['cb_c'])

        if 'tad_z1' in kwargs:
            self.tad_xfmr.load_kw(z1=kwargs['tad_z1'])

        if 'tad_z2' in kwargs:
            self.tad_xfmr.load_kw(z2=kwargs['tad_z2'])

        if 'tad_z3' in kwargs:
            self.tad_xfmr.load_kw(z3=kwargs['tad_z3'])

        if 'tad_zc' in kwargs:
            self.tad_xfmr.load_kw(zc=kwargs['tad_zc'])

        if 'tad_n' in kwargs:
            self.tad_xfmr.load_kw(n=kwargs['tad_n'])

        if 'ba_z' in kwargs:
            self.ba.load_kw(z=kwargs['ba_z'])

        if 'ca_z' in kwargs:
            self.ca.load_kw(z=kwargs['ca_z'])

        if 'fl_param' in kwargs:
            self.fl_xfmr.load_kw(z1=kwargs['fl_param'].z1)
            self.fl_xfmr.load_kw(z2=kwargs['fl_param'].z2)
            self.fl_xfmr.load_kw(n=kwargs['fl_param'].n)

        if 'tad_param' in kwargs:
            self.fl_xfmr.load_kw(z1=kwargs['tad_param'].z1)
            self.fl_xfmr.load_kw(z2=kwargs['tad_param'].z2)
            self.fl_xfmr.load_kw(z3=kwargs['tad_param'].z3)
            self.fl_xfmr.load_kw(zc=kwargs['tad_param'].zc)
            self.fl_xfmr.load_kw(n=kwargs['tad_param'].n)

        if 'cb_param' in kwargs:
            self.cable.load_kw(R=kwargs['cb_param'].R)
            self.cable.load_kw(L=kwargs['cb_param'].L)
            self.cable.load_kw(C=kwargs['cb_param'].C)

    def create_circuit(self):
        length = len(self.modules) - 1
        for index in range(length):
            m1 = self.modules[index]
            m2 = self.modules[index + 1]
            m1.ports[-2].link_node(m2.ports[0])
            m1.ports[-1].link_node(m2.ports[1])

    def create_port(self):
        self.config_port(self.modules[-1].ports[-2], self.modules[-1].ports[-1])

    def config_param(self, freq):
        for ele in self.modules():
            ele.config_param(freq)

    def init_param(self, params):

        self.load_kw(z_pwr=params['Param_Z_Power'])
        self.load_kw(z_rcv=params['Param_Z_Rcv'])

        self.load_kw(fl_param=params['Param_FL_Snd'])

        self.load_kw(cb_param=params['Param_Cable'])

        self.load_kw(tad_param=params['Param_TAD_Snd_QJ'])
        self.load_kw(tad_zc=params['Param_TAD_Snd_ZN'].zc)

        self.load_kw(ba_z=params['Param_PT'])

        self.load_kw(ca_z=params['Param_CA_QJ'])
