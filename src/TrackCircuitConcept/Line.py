from src.TrackCircuitConcept.Rail import RailGroup
from src.Unit.BasicUnit import UnitGroup
from src.Unit.TrackUnit import TrackUnit


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

        self._all_units = UnitGroup(set())
        self._track_units = UnitGroup(set())
        self._pos_set = set()
        self._track_node = None


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

    def get_all_units(self):
        all_units = set()
        for ele in self.element:
            all_units.update(ele.get_all_units())
        self._all_units.set_units(all_units)
        return all_units

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        tmp.update(self.rails.pos_set)
        tmp.update(self._all_units.pos_set)
        return tmp

    def init_track(self, pos_set=None):
        if pos_set is None:
            pos_set = self.pos_set
        if isinstance(pos_set, set):
            tmp = self._track_units
            tmp.clear()
            pos_list = list(pos_set)
            pos_list.sort()
            pos_list = pos_list[1:-1]
            for index in range(len(pos_list)-1):
                l_pos = pos_list[index]
                r_pos = pos_list[index + 1]
                name = '钢轨段%s' % (index+1)
                unit = TrackUnit(self, name)
                unit.load_kwargs(l_pos=l_pos, r_pos=r_pos)
                tmp.add(unit)

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

        self._all_units = UnitGroup(set())
        self._pos_set = set()
        self._track_units = set()

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

    def get_all_units(self):
        self._all_units.clear()
        all_units = set()
        for line in self.lines:
            all_units.update(line.get_all_units())

        self._all_units.set_units(all_units)
        return all_units

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        for line in self.lines:
            tmp.update(line.pos_set)
        return tmp

    def init_track(self):
        for line in self.lines:
            line.init_track(pos_set=self.pos_set)

    @property
    def track_units(self):
        return self._track_units