from src.Module.BasicModule import BasicModule
from src.Module.ElectricModule import ImpedanceModule
from src.Module.ElectricModule import XfmrModule
from src.Module.ElectricModule import TCircuitModule
from src.Module.ElectricModule import CableModule
from src.CircuitConcept.Edge import VolSrcEdge
from src.CircuitConcept.Edge import WireEdge
from src.CircuitConcept.Edge import ImpedanceEdge
from src.CircuitConcept.Port import Port


class TcsrXfmr(BasicModule):
    """
        TCSR变压器
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)
        self.m1 = TCircuitModule(self, '1等效内阻')
        self.m2 = XfmrModule(self, '2理想变压器')

        self.m2.w1.load_kwargs(bas_name='1室内侧')
        self.m2.w2.load_kwargs(bas_name='2室外侧')

        self.add_element(self.m1, self.m2)
        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):
        if 'z1' in kwargs:
            self.m1.load_kw(z1=kwargs['z1'])

        if 'z2' in kwargs:
            self.m1.load_kw(z2=kwargs['z2'])

        if 'z3' in kwargs:
            self.m1.load_kw(z3=kwargs['z3'])

        if 'n' in kwargs:
            self.m2.load_kw(n=kwargs['n'])

    def create_circuit(self):
        self.m1.ports[2].link_node(self.m2.ports[0])
        self.m1.ports[3].link_node(self.m2.ports[1])

    def create_port(self):
        self.config_port(self.m1.ports[0], self.m1.ports[1],
                         self.m2.ports[2], self.m2.ports[3])

    def config_param(self, freq):
        self.m1.config_param(freq)
        self.m2.config_param(freq)


class TcsrFLXfmr(TcsrXfmr):
    """
        防雷变压器
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):
        if 'z1' in kwargs:
            self.m1.load_kw(z1=kwargs['z1'], z3=kwargs['z1'])

        if 'z2' in kwargs:
            self.m1.load_kw(z2=kwargs['z2'])

        if 'n' in kwargs:
            self.m2.load_kw(n=kwargs['n'])


class TcsrTADXfmr(BasicModule):
    """
        TAD变压器
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)
        self._param = [None] * 2

        self.l1 = ImpedanceEdge(self, '1共模电感')
        self.m1 = TcsrXfmr(self, '2变压器')
        self.c1 = ImpedanceEdge(self, '3电容')

        self.add_element(self.l1, self.m1, self.c1)
        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):
        if 'z1' in kwargs:
            self.m1.load_kw(z1=kwargs['z1'], z3=kwargs['z1'])

        if 'z2' in kwargs:
            self.m1.load_kw(z2=kwargs['z2'])

        if 'n' in kwargs:
            self.m1.load_kw(n=kwargs['n'])

        if 'z3' in kwargs:
            self._param[0] = kwargs['z3']

        if 'zc' in kwargs:
            self._param[1] = kwargs['zc']

    @property
    def z3(self):
        return self.param[0]

    @property
    def zc(self):
        return self.param[1]

    # def create_circuit(self):
    #     self.l1.ports[1].link_node(self.m1.ports[0])
    #     self.c1.ports[0].link_node(self.m1.ports[2])
    #
    # def create_port(self):
    #     self.config_port(self.l1.ports[0], self.m1.ports[1],
    #                      self.c1.ports[1], self.m1.ports[3])

    def create_circuit(self):
        self.l1.end.link_node(self.m1.ports[0])
        self.c1.start.link_node(self.m1.ports[2])

    def create_port(self):
        # self.config_port(Port(self.l1, True), self.m1.ports[1],
        #                  Port(self.c1, False), self.m1.ports[3])

        self.config_port(self.l1.start, self.m1.ports[1].node,
                         self.c1.end, self.m1.ports[3].node)

    def config_param(self, freq):
        self.l1.config_param(self.z3.z(freq))
        self.c1.config_param(self.zc.z(freq))
        self.m1.config_param(freq)


class TcsrPower(BasicModule):
    """
        功出电源
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)
        # self._param = [None] * 2
        self._param = [180, None]

        self.u1 = VolSrcEdge(self, '1理想电压源')
        self.r1 = ImpedanceEdge(self, '2内阻')

        self.add_element(self.u1, self.r1)
        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):
        if 'u_pwr' in kwargs:
            self._param[0] = kwargs['u_pwr']

        if 'z_pwr' in kwargs:
            self._param[1] = kwargs['z_pwr']

    @property
    def u_pwr(self):
        return self.param[0]

    @property
    def z_pwr(self):
        return self.param[1]

    @property
    def snd_lvl(self):
        return self.parent.snd_lvl

    # def create_circuit(self):
    #     self.u1.start.link_node(self.r1.ports[0])
    #
    # def create_port(self):
    #     self.config_port(self.r1.ports[1], Port(self.u1, False))

    def create_circuit(self):
        self.u1.start.link_node(self.r1.start)

    def create_port(self):
        # self.config_port(Port(self.r1, False), Port(self.u1, False))

        self.config_port(self.r1.end, self.u1.end)

    def config_param(self, freq):
        self.u1.config_param(self.u_pwr)
        self.r1.config_param(self.z_pwr[self.snd_lvl].z(freq))


class TcsrReceiver(ImpedanceModule):
    """
        接收器
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)
        self.load_kw(**kwargs)


class TcsrBA(ImpedanceModule):
    """
        匹配单元
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)
        self.load_kw(**kwargs)

    @property
    def z(self):
        return self.param[0][self.main_freq]

    def config_param(self, freq):
        self.r1.config_param(self.z.z(freq))

    @property
    def main_freq(self):
        return self.parent.m_freq


class TcsrCA(BasicModule):
    """
        引接线
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name)
        self._param = [None]

        self.r1 = ImpedanceEdge(self, '1电阻')
        self.wr1 = WireEdge(self, '2导线')

        self.add_element(self.r1, self.wr1)
        self.create_circuit()
        self.create_port()

        self.load_kw(**kwargs)

    def load_kw(self, **kwargs):
        if 'z' in kwargs:
            self._param[0] = kwargs['z']

    @property
    def z(self):
        return self.param[0]

    def create_circuit(self):
        pass

    def create_port(self):
        # self.config_port(Port(self.r1, True), Port(self.wr1, True),
        #                  Port(self.r1, False), Port(self.wr1, False))

        self.config_port(self.r1.start, self.wr1.start,
                         self.r1.end, self.wr1.end)

    def config_param(self, freq):
        self.r1.config_param(self.z.z(freq))


class TcsrCable(CableModule):
    """
        发送接收电缆
    """

    def __init__(self, parent, bas_name, **kwargs):
        super().__init__(parent, bas_name, **kwargs)

    @property
    def length(self):
        return self.parent.cable_len
