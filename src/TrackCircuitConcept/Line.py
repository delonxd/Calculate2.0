from src.TrackCircuitConcept.Rail import RailGroup
from src.Unit.UnitGroup import UnitSet
from src.Unit.TrackUnit import TrackUnit
from src.TrackCircuitConcept.TrackNode import TrackNode

from src.Module.ModuleGroup import ModuleSet
from src.CircuitConcept.EdgeGroup import EdgeSet
from src.CircuitConcept.NodeGroup import NodeSet


class Line:
    """
        线路类型
    """

    def __init__(self, parent, bas_name, **kwargs):
        self.parent = parent
        self._bas_name = bas_name
        self._name = None
        self.rails = RailGroup()
        self.element = list()

        self._ele_units = UnitSet()
        self._track_units = UnitSet()

        self._pos_set = set()
        self._track_nodes = dict()

        self._all_modules = ModuleSet()
        self._all_edges = EdgeSet()
        self._all_nodes = NodeSet()

        self.load_kwargs(**kwargs)

    @property
    def rlt_pos(self):
        return 0

    @property
    def abs_pos(self):
        return 0

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

    def add_element(self, ele):
        self.element.append(ele)
        ele.parent = self

    def load_kwargs(self, **kwargs):
        if 'rails' in kwargs:
            rails = kwargs['rails']
            if isinstance(rails, RailGroup):
                self.rails = rails

        if 'elements' in kwargs:
            elements = kwargs['elements']
            for ele in elements:
                self.add_element(ele)

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        tmp.update(self.rails.pos_set)
        tmp.update(self._ele_units.pos_set)
        return tmp

    @property
    def ele_units(self):
        return self._ele_units

    @property
    def track_units(self):
        return self._track_units

    def get_all_modules(self):
        tmp = self._all_modules
        tmp.clear()
        tmp.update(self.ele_units.get_all_modules())
        tmp.update(self.track_units.get_all_modules())
        return tmp

    def get_all_edges(self):
        tmp = self._all_edges
        tmp.clear()
        modules = self._all_modules
        tmp.update(modules.get_all_edges())
        return tmp

    def get_all_nodes(self):
        tmp = self._all_nodes
        tmp.clear()
        edges = self._all_edges
        tmp.update(edges.get_all_nodes())
        return tmp

    def get_all_vars(self):
        from src.CircuitConcept.Variable import VarSet
        tmp = VarSet()

        tmp.update(self._all_nodes.get_all_var())
        tmp.update(self._all_edges.get_all_var())
        return tmp

    def init_unit(self):
        tmp = self._ele_units
        tmp.clear()
        for ele in self.element:
            ele.init_unit()
            tmp.update(ele.get_all_units())

    def init_track_nodes(self, pos_set=None):
        if pos_set is None:
            pos_set = self.pos_set
        if isinstance(pos_set, set):
            tmp = self._track_nodes
            tmp.clear()
            pos_list = list(pos_set)
            pos_list.sort()
            pos_list = pos_list[1:-1]
            for pos in pos_list:
                track_node = TrackNode(parent=self, pos=pos)
                tmp[pos] = track_node

    def init_track(self):
        tmp = self._track_units
        tmp.clear()
        nodes = self._track_nodes
        keys = list(nodes.keys())
        keys.sort()
        for index in range(len(keys)-1):
            l_pos = keys[index]
            r_pos = keys[index + 1]
            name = '钢轨段%s' % (index+1)
            unit = TrackUnit(self, name)
            unit.load_kwargs(l_pos=l_pos, r_pos=r_pos)
            nodes[l_pos].r_track = unit
            nodes[r_pos].l_track = unit
            tmp.add(unit)

        from src.Unit.OutsideUnit import BreakPoint
        from src.TrackCircuitConcept.TrackNode import BreakNode

        for unit in self._ele_units:
            node = nodes[unit.abs_pos]
            if isinstance(unit, BreakPoint):
                node._mode = BreakNode
            else:
                node.units.add(unit)

    def link_track(self):
        for node in self._track_nodes.values():
            node.link_nodes()

    def create_module(self):
        self.ele_units.create_module()
        self.track_units.create_module()

    def init_param(self, param_dict):
        self._all_modules.init_param(param_dict)

    def config_param(self, freq):
        self._all_modules.config_param(freq)


class LineGroup:
    """
        线路组类型
    """

    def __init__(self, parent, bas_name, **kwargs):
        self.parent = parent
        self._bas_name = bas_name
        self._name = None
        self.lines = list()

        self._ele_units = UnitSet()
        # self._all_units = UnitGroup(set())
        self._pos_set = set()
        self._track_units = UnitSet()

        self.load_kwargs(**kwargs)

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

    def add_line(self, line):
        if isinstance(line, Line):
            self.lines.append(line)
            line.parent = self

    def load_kwargs(self, **kwargs):
        if 'lines' in kwargs:
            lines = kwargs['lines']
            for line in lines:
                if isinstance(line, Line):
                    self.add_line(line)

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        for line in self.lines:
            tmp.update(line.pos_set)
        return tmp

    @property
    def ele_units(self):
        tmp = self._ele_units
        tmp.clear()
        for line in self.lines:
            tmp.update(line.ele_units)
        return tmp

    @property
    def track_units(self):
        return self._track_units

    def init_unit(self):
        for line in self.lines:
            line.init_unit()

    def init_track_nodes(self):
        for line in self.lines:
            line.init_track_nodes(pos_set=self.pos_set)

    def init_track(self):
        for line in self.lines:
            line.init_track()

    def link_track(self):
        for line in self.lines:
            line.link_track()

    def create_module(self):
        for line in self.lines:
            line.create_module()
