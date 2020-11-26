from src.CircuitConcept.Variable import Variable
from src.CircuitConcept.Node import Node


class Edge:
    """
        边
    """

    def __init__(self, parent, base_name):
        self.parent = parent

        self.start = Node()
        self.end = Node()
        # self.start.edges.append((True, self))
        # self.end.edges.append((False, self))
        self.start.edges.add(self)
        self.end.edges.add(self)

        self._bas_name = base_name
        self._name = ''

        self.variable = Variable()
        self.variable_type = 'I'

    @property
    def bas_name(self):
        if self._bas_name is None:
            return ''
        else:
            return self._bas_name

    @property
    def name(self):
        if self.parent is None:
            return self.bas_name
        else:
            name = self.parent.name + '_' + self.bas_name
            self._name = name
            return name

    @property
    def current(self):
        return self.variable.value

    @property
    def voltage(self):
        voltage = self.start.voltage - self.end.voltage
        return voltage

    def load_kwargs(self, **kwargs):
        if 'bas_name' in kwargs:
            self._bas_name = kwargs['bas_name']


class ImpedanceEdge(Edge):
    def __init__(self, parent, base_name):
        super().__init__(parent, base_name)
        self._z = None

    @property
    def z(self):
        return self._z

    def config_param(self, param):
        self._z = param


class WindingEdge(Edge):
    def __init__(self, parent, base_name):
        super().__init__(parent, base_name)
        self._other = None
        self._n = None
        # self.source = True

    @property
    def other(self):
        return self._other

    @property
    def n(self):
        return self._n

    def config_param(self, other, n):
        self._other = other
        self._n = n


class VolSrcEdge(Edge):
    def __init__(self, parent, base_name):
        super().__init__(parent, base_name)
        # self.type = '电压源'
        self._vol = None

    @property
    def vol(self):
        return self._vol

    def config_param(self, vol):
        self._vol = vol


class CurSrcEdge(Edge):
    def __init__(self, parent, base_name):
        super().__init__(parent, base_name)
        self.type = '电流源'
        self._cur = None

    @property
    def cur(self):
        return self._cur

    def config_param(self, cur):
        self._cur = cur


class WireEdge(Edge):
    def __init__(self, parent, base_name):
        super().__init__(parent, base_name)
        self.type = '导线'

    def config_param(self):
        pass
