class BasicUnit:
    """
        轨面单元
    """

    def __init__(self, parent,  **kwargs):
        self.parent = parent

        self._bas_name = None
        self._rlt_pos = None
        self._md_type = None
        self.module = None

        # generated
        self._name = str()
        self.load_kwargs(**kwargs)

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

    @property
    def md_type(self):
        return self._md_type

    def create_module(self):
        self.module = self.md_type(self)

    def load_kwargs(self, **kwargs):

        if 'rlt_pos' in kwargs:
            self._rlt_pos = kwargs['rlt_pos']

        if 'bas_name' in kwargs:
            self._bas_name = kwargs['bas_name']

    def load_param(self):
        pass


class UnitGroup:
    """
        轨面单元组
    """
    
    def __init__(self, unit_set):
        self.unit_set: set = unit_set
        self._unit_list = list()

        self._pos_set = set()
        self._name_list = list()

    def set_units(self, value):
        self.unit_set.clear()
        self.unit_set.update(value)

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        for unit in self.unit_set:
            tmp.add(unit.abs_pos)
        return tmp

    @property
    def name_list(self):
        tmp = list()
        for unit in self.unit_set:
            tmp.append(unit.name)
        self._name_list = tmp
        return self._name_list

    # def get_unit_pos(self):
    #     unit_list = list()
    #     for unit in self.unit_set:
    #         abs_pos = unit.abs_pos
    #         unit_list.append((abs_pos, unit))
    #     unit_list.sort()
    #     self._unit_list = unit_list
    #     return unit_list

    def create_module(self):
        for unit in self.unit_set:
            unit.create_module()

    def init_param(self, param_dict):
        for unit in self.unit_set:
            unit.module.init_param(param_dict)

    def clear(self):
        self.unit_set.clear()
        self._unit_list.clear()
