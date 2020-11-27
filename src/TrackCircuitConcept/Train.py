from src.Unit.OutsideUnit import RShort
from src.Unit.UnitGroup import UnitSet


class Train:
    """
        列车类型
    """

    def __init__(self, parent, bas_name, **kwargs):
        self.parent = parent
        self._bas_name = bas_name
        self._rlt_pos = None

        self._name = None
        self.units = UnitSet()

        self.load_kwargs(**kwargs)

    @property
    def r_short(self):
        for unit in self.units:
            return unit
        return None

    @property
    def rlt_pos(self):
        if self._rlt_pos is None:
            return 0
        else:
            return self._rlt_pos

    @property
    def abs_pos(self):
        if self.parent is None:
            return self.rlt_pos
        else:
            pos = self.parent.abs_pos + self.rlt_pos
            return pos

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
        if 'rlt_pos' in kwargs:
            self._rlt_pos = kwargs['rlt_pos']

    def init_unit(self):
        self.units.clear()
        unit = RShort(self, '轮对')
        self.units.add(unit)

    def get_all_units(self):
        all_units = self.units
        return all_units
