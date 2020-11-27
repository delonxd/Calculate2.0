# from src.CircuitConcept.Variable import Variable
from src.CircuitConcept.Variable import VoltageVar
from src.Equation.Equation import Equation


class Node:
    """
        节点
    """

    def __init__(self):

        from src.CircuitConcept.EdgeGroup import EdgeSet
        self.edges = EdgeSet()

        self.variable = VoltageVar(self)
        self.gnd_flg = False

    @property
    def voltage(self):
        return self.variable.value

    @property
    def voltage_abs(self):
        return self.variable.value_abs

    @property
    def name(self):
        for edge in self.edges:
            if self == edge.start:
                return edge.name + '_起点'
            else:
                return edge.name + '_终点'
        return ''

    def get_equation(self):
        equ = Equation()

        if self.gnd_flg is True:
            equ.append_coeff(self.variable, 1)

        else:
            for edge in self.edges:
                if self is edge.start:
                    value = 1
                else:
                    value = -1

                equ.append_coeff(edge.variable, value)

        return equ

    # def link_edge(self, edge, outflow: bool = True):
    #     if isinstance(edge, Edge):
    #         self.edges.append((outflow, edge))
    #         if outflow:
    #             edge.start = self
    #         else:
    #             edge.end = self
    #     else:
    #         raise KeyboardInterrupt("类型异常：需要边类型")

    def link_edge(self, edge, outflow: bool = True):
        from src.CircuitConcept.Edge import Edge

        if isinstance(edge, Edge):
            self.edges.add(edge)
            if outflow:
                edge.start = self
            else:
                edge.end = self
        else:
            raise KeyboardInterrupt("类型异常：需要边类型")

    def link_node(self, other):
        from src.CircuitConcept.Port import Port

        if isinstance(other, Node):
            for edge in other.edges:
                self.edges.add(edge)
                if edge.start == other:
                    edge.start = self
                else:
                    edge.end = self
        elif isinstance(other, Port):
            self.link_node(other.node)
        else:
            raise KeyboardInterrupt("类型异常：需要节点类型")

    # def link_node(self, other):
    #     if isinstance(other, Node):
    #         for outflow, edge in other.edges:
    #             self.edges.append((outflow, edge))
    #             if outflow:
    #                 edge.start = self
    #             else:
    #                 edge.end = self
    #     elif isinstance(other, Port):
    #         self.link_node(other.node)
    #     else:
    #         raise KeyboardInterrupt("类型异常：需要节点或端口类型")
