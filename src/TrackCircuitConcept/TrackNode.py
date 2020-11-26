from src.Unit.UnitGroup import UnitSet


class TrackNode:
    """
        钢轨节点
    """

    def __init__(self, **kwargs):
        self.parent = None
        self.pos = None
        self.units = UnitSet()
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
                return NoneTrack
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
            port1 = self.r_track.module.ports[0]
            port2 = self.r_track.module.ports[1]
        elif self.mode is RightNode:
            port1 = self.l_track.module.ports[2]
            port2 = self.l_track.module.ports[3]
        elif self.mode is ConnectNode:
            port1 = self.l_track.module.ports[2]
            port2 = self.l_track.module.ports[3]
        else:
            port1 = None
            port2 = None
        return port1, port2

    def link_nodes(self):
        l_track = self.l_track
        r_track = self.r_track

        mode = self.mode

        if mode is NoneTrack:
            pass

        elif mode is BreakNode:
            from src.Unit.BasicUnit import BP_Left, BP_Right

            pos = self.pos
            for unit in self.units:
                flg = unit.bp_flg(pos)
                if flg == BP_Left:
                    unit.module.ports[-2].link_node(l_track.module.ports[2])
                    unit.module.ports[-1].link_node(l_track.module.ports[3])
                elif flg == BP_Right:
                    unit.module.ports[-2].link_node(r_track.module.ports[0])
                    unit.module.ports[-1].link_node(r_track.module.ports[1])

        else:
            port1, port2 = self.ports
            for unit in self.units:
                unit.module.ports[-2].link_node(port1)
                unit.module.ports[-1].link_node(port2)

            if mode is ConnectNode:
                l_track.module.ports[2].link_node(r_track.module.ports[0])
                l_track.module.ports[3].link_node(r_track.module.ports[1])


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


class NoneTrack(NodeType):
    """
        无钢轨相连
    """