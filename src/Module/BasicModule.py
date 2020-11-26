from src.CircuitConcept.Port import Port
from src.CircuitConcept.Edge import Edge


class BasicModule:
    """
        基础模块
    """

    def __init__(self, parent, bas_name, **kw):
        # structure
        self.parent = parent

        # parameters
        self._bas_name = bas_name
        self._param = list()

        # generated
        self._name = str()
        self.ports = list()

        from src.Module.ModuleGroup import ModuleList
        from src.CircuitConcept.EdgeGroup import EdgeList

        self.modules = ModuleList()
        self.edges = EdgeList()
        # self.edges_all = list()

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
    def param(self):
        return self._param

    def load_kw(self, **kwargs):
        """

        """

        if 'param' in kwargs:
            self._param = kwargs['param']

    def get_all_edges(self):
        from src.CircuitConcept.EdgeGroup import EdgeSet
        tmp = EdgeSet(self.edges)
        tmp.update(self.modules.get_all_edges())
        return tmp

    def get_all_nodes(self):
        tmp = self.get_all_edges()
        node_set = tmp.get_all_nodes()
        return node_set

    def config_port(self, *ports):
        for port in ports:
            if isinstance(port, Port):
                self.ports.append(port)
            else:
                raise KeyboardInterrupt("类型异常：需要Port类型")

    def add_element(self, *element):
        for ele in element:
            if isinstance(ele, Edge):
                self.edges.append(ele)
                ele.parent = self
            elif isinstance(ele, BasicModule):
                self.modules.append(ele)
                ele.parent = self
            else:
                raise KeyboardInterrupt("类型异常：需要Edge或Module类型")

    # def config_edge_para(self, freq):
    #     pass
    #
    # def config_parameter(self, freq):
    #     for md in self.modules:
    #         md.config_parameter(freq)
    #     self.config_edge_para(freq)

    def create_circuit(self):
        pass

    def create_port(self):
        pass

    def config_param(self, freq):
        pass


if __name__ == '__main__':
    pass
