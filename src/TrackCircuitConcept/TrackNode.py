from src.Unit.UnitGroup import UnitGroup


class TrackNode:
    """
        钢轨节点
    """

    def __init__(self, **kwargs):
        self.parent = None
        self.pos = None
        self.units = UnitGroup()
        self.l_track = None
        self.r_track = None

        self._mode = ConnectNode

        self.load_kwargs(**kwargs)

    def add_unit(self, unit):
        self.units.add(unit)

    def load_kwargs(self, **kwargs):
        if 'parent' in kwargs:
            self.pos = kwargs['parent']

        if 'pos' in kwargs:
            self.pos = kwargs['pos']

        if 'l_track' in kwargs:
            self.l_track = kwargs['l_track']

        if 'r_track' in kwargs:
            self.r_track = kwargs['r_track']

        if 'units' in kwargs:
            self.units = kwargs['units']

    @property
    def mode(self):
        if self.l_track is None:
            if self.r_track is None:
                return None
            else:
                return LeftNode
        else:
            if self.l_track is None:
                return RightNode
            else:
                return self._mode

    @property
    def ports(self):
        if self.mode is LeftNode:
            port1 = self.r_track.module.port[0]
            port2 = self.r_track.module.port[1]
        elif self.mode is RightNode:
            port1 = self.l_track.module.port[2]
            port2 = self.l_track.module.port[3]
        elif self.mode is ConnectNode:
            port1 = self.l_track.module.port[2]
            port2 = self.l_track.module.port[3]
        else:
            port1 = None
            port2 = None
        return port1, port2

    def link_nodes(self):
        l_track = self.l_track
        r_track = self.r_track

        if self.mode is BreakNode:
            pass

        else:
            port1, port2 = self.ports
            for unit in self.units:
                unit.module.port[0].link_node(port1)
                unit.module.port[1].link_node(port2)

            if self.mode is ConnectNode:
                l_track.module.port[2].link_node(r_track.module.port[0])
                l_track.module.port[3].link_node(r_track.module.port[1])

    def link_break_point(self):
        for _ in self.units:
            pass


class NodeType:
    """
        节点类型
    """


class BreakNode(NodeType):
    """
        双断节点
    """


class ConnectNode(NodeType):
    """
        中间节点
    """


class LeftNode(NodeType):
    """
        左侧节点
    """


class RightNode(NodeType):
    """
        右侧节点
    """