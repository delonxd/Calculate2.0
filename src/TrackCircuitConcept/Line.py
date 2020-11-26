from src.TrackCircuitConcept.Rail import RailGroup
# from src.Unit.BasicUnit import UnitGroup
from src.Unit.UnitGroup import UnitGroup
from src.Unit.TrackUnit import TrackUnit
from src.TrackCircuitConcept.TrackNode import TrackNode


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

        # self._all_units = UnitGroup(set())
        self._ele_units = UnitGroup()
        self._pos_set = set()
        self._track_nodes = dict()
        self._track_units = UnitGroup()

        self.load_kwargs(**kwargs)

    @property
    def rlt_pos(self):
        return 0

    @property
    def abs_pos(self):
        return 0

    def add_element(self, ele):
        self.element.append(ele)
        ele.parent = self

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

    def load_kwargs(self, **kwargs):
        if 'rails' in kwargs:
            rails = kwargs['rails']
            if isinstance(rails, RailGroup):
                self.rails = rails

        if 'elements' in kwargs:
            elements = kwargs['elements']
            for ele in elements:
                self.add_element(ele)

    def init_unit(self):
        for ele in self.element:
            ele.init_unit()

    @property
    def ele_units(self):
        tmp = self._ele_units
        tmp.clear()
        for ele in self.element:
            tmp.update(ele.get_all_units())
        return tmp

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        tmp.update(self.rails.pos_set)
        tmp.update(self._ele_units.pos_set)
        return tmp

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
            if isinstance(unit, BreakPoint):
                nodes._mode = BreakNode
            else:
                nodes[unit.abs_pos].units.add(unit)

    @property
    def track_units(self):
        return self._track_units

    def link_track(self):
        pass


class LineGroup:
    """
        线路组类型
    """

    def __init__(self, parent, bas_name, **kwargs):
        self.parent = parent
        self._bas_name = bas_name
        self._name = None
        self.lines = list()

        self._ele_units = UnitGroup()
        # self._all_units = UnitGroup(set())
        self._pos_set = set()
        self._track_units = UnitGroup()

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

    def init_unit(self):
        for line in self.lines:
            line.init_unit()

    # def get_all_units(self):
    #     self._all_units.clear()
    #     all_units = set()
    #     for line in self.lines:
    #         all_units.update(line.get_all_units())
    #
    #     self._all_units.set_units(all_units)
    #     return all_units

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        for line in self.lines:
            tmp.update(line.pos_set)
        return tmp

    def init_track_nodes(self):
        for line in self.lines:
            line.init_track_nodes(pos_set=self.pos_set)

    def init_track(self):
        for line in self.lines:
            line.init_track()

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