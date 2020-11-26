class UnitGroup(set):
    """
        单元组
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pos_set = set()
        self._name_list = list()

    @property
    def pos_set(self):
        tmp = self._pos_set
        tmp.clear()
        for unit in self:
            tmp.add(unit.abs_pos)
        return tmp

    @property
    def name_list(self):
        tmp = self._name_list
        tmp.clear()
        for unit in self:
            tmp.append(unit.name)
        return self._name_list

    def create_module(self):
        for unit in self:
            unit.create_module()

    def init_param(self, param_dict):
        for unit in self:
            if unit.module:
                unit.module.init_param(param_dict)

    def config_param(self, freq):
        for unit in self:
            print(unit.name)
            if unit.module:
                unit.module.config_param(freq)
