from src.Module.BasicModule import BasicModule
from src.Module.TcsrModule import TcsrPower
from src.Module.TcsrModule import TcsrReceiver
from src.Module.TcsrModule import TcsrFLXfmr
from src.Module.ElectricModule import CableModule
from src.Module.TcsrModule import TcsrTADXfmr
from src.Module.TcsrModule import TcsrBA
from src.Module.TcsrModule import TcsrCA
from src.Module.TcsrModule import TcsrCable
from src.Module.ElectricModule import ImpedanceModule


class BasicTCSR(BasicModule):
    """
        基础发送接收模块
    """
    def __init__(self, parent, bas_name):
        super().__init__(parent, bas_name)

    @property
    def m_freq(self):
        return self.parent.m_freq

    @property
    def snd_lvl(self):
        return self.parent.snd_lvl

    @property
    def cable_len(self):
        return self.parent.cable_len

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
        for ele in self.modules:
            ele.config_param(freq)


class ZPW2000A_TCSR_QJ_Normal(BasicTCSR):
    """
        2000A区间发送接收标准模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = 'ZPW2000A区间模块'
        super().__init__(parent, bas_name)

        self.power = TcsrPower(self, '1发送器')
        self.receiver = TcsrReceiver(self, '1接收器')
        self.fl_xfmr = TcsrFLXfmr(self, '2FL')
        # self.cable = CableModule(self, '3电缆')
        self.cable = TcsrCable(self, '3电缆')
        self.tad_xfmr = TcsrTADXfmr(self, '4TAD')
        self.ba = TcsrBA(self, '5PT')
        self.ca = TcsrCA(self, '6CA')

        self.init_element()
        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def init_element(self):
        from src.Unit.TcsrUnit import Snd_Mde, Rcv_Mde

        if self.parent.mode == Snd_Mde:
            self.add_element(self.power)
        elif self.parent.mode == Rcv_Mde:
            self.add_element(self.receiver)
        self.add_element(self.fl_xfmr)
        self.add_element(self.cable)
        self.add_element(self.tad_xfmr)
        self.add_element(self.ba)
        self.add_element(self.ca)

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
            self.tad_xfmr.load_kw(z1=kwargs['tad_param'].z1)
            self.tad_xfmr.load_kw(z2=kwargs['tad_param'].z2)
            self.tad_xfmr.load_kw(z3=kwargs['tad_param'].z3)
            self.tad_xfmr.load_kw(zc=kwargs['tad_param'].zc)
            self.tad_xfmr.load_kw(n=kwargs['tad_param'].n)

        if 'cb_param' in kwargs:
            self.cable.load_kw(R=kwargs['cb_param'].R)
            self.cable.load_kw(L=kwargs['cb_param'].L)
            self.cable.load_kw(C=kwargs['cb_param'].C)

    def init_param(self, param_dict):
        param = param_dict
        self.load_kw(z_pwr=param['Param_Z_Power'])

        self.load_kw(z_rcv=param['Param_Z_Rcv'])

        self.load_kw(fl_param=param['Param_FL_Snd'])

        self.load_kw(cb_param=param['Param_Cable'])

        self.load_kw(tad_param=param['Param_TAD_Snd_QJ'])

        self.load_kw(tad_zc=param['Param_TAD_Snd_ZN'].zc)

        self.load_kw(ba_z=param['Param_PT'])

        self.load_kw(ca_z=param['Param_CA_QJ'])


class ZPW2000A_TCSR_ZN_PT_SVA1(ZPW2000A_TCSR_QJ_Normal):
    """
        2000A站内发送接收PT+SVA模块
    """

    def __init__(self, parent, **kwargs):
        bas_name = 'ZPW2000A站内PTSVA1模块'
        BasicModule.__init__(self, parent, bas_name)

        self.power = TcsrPower(self, '1发送器')
        self.receiver = TcsrReceiver(self, '1接收器')
        self.fl_xfmr = TcsrFLXfmr(self, '2FL')
        # self.cable = CableModule(self, '3电缆')
        self.cable = TcsrCable(self, '3电缆')
        self.tad_xfmr = TcsrTADXfmr(self, '4TAD')
        self.ba = TcsrBA(self, '5PT')
        self.sva1 = ImpedanceModule(self, '6SVA1')
        self.ca = TcsrCA(self, '7CA')

        self.init_element()
        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def init_element(self):
        from src.Unit.TcsrUnit import Snd_Mde, Rcv_Mde

        if self.parent.mode == Snd_Mde:
            self.add_element(self.power)
        elif self.parent.mode == Rcv_Mde:
            self.add_element(self.receiver)
        self.add_element(self.fl_xfmr)
        self.add_element(self.cable)
        self.add_element(self.tad_xfmr)
        self.add_element(self.ba)
        self.add_element(self.sva1)
        self.add_element(self.ca)

    def load_kw(self, **kwargs):
        super().load_kw(**kwargs)

        if 'sva1_z' in kwargs:
            self.sva1.load_kw(z=kwargs['sva1_z'])

    def init_param(self, param_dict):
        super().init_param(param_dict)

        self.load_kw(sva1_z=param_dict['Param_SVA_Plus'])
