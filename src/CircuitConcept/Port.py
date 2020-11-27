from src.CircuitConcept.Edge import PortEdge
from src.CircuitConcept.Node import Node


class Port:
    """
        端口
    """

    def __init__(self, parent, node: Node):
        self.parent = parent
        self._node = Node()
        self.edge = PortEdge(self, '端口连接')
        # self.start_flag = flag

        self.node.link_node(self.edge.start)
        node.link_node(self.edge.end)

    @property
    def node(self):
        # if self.start_flag:
        #     return self.edge.start
        # else:
        #     return self.edge.end
        return self._node

    def link_node(self, other):
        self.node.link_node(other)

    @property
    def voltage(self):
        return self.node.voltage
