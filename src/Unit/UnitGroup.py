from src.Unit.BasicUnit import BasicUnit


class UnitSet(set):
    """
        单元集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pos_set = set()
        self._name_list = list()

    def add(self, obj):
        if isinstance(obj, BasicUnit):
            super().add(obj)
        else:
            raise KeyboardInterrupt("%s应为BasicUnit类型" % obj)

    def update(self, obj):
        if isinstance(obj, UnitSet):
            super().update(obj)
        else:
            raise KeyboardInterrupt("%s应为UnitSet类型" % obj)

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
        tmp.sort()
        return self._name_list

    def get_all_modules(self):
        from src.Module.ModuleGroup import ModuleSet
        tmp = ModuleSet()

        for unit in self:
            if unit.module is not None:
                tmp.add(unit.module)
        return tmp

    def get_all_edges(self):
        tmp = self.get_all_modules()
        edge_set = tmp.get_all_edges()
        return edge_set

    def get_all_nodes(self):
        tmp = self.get_all_edges()
        node_set = tmp.get_all_nodes()
        return node_set

    def create_module(self):
        for unit in self:
            unit.create_module()

    def init_param(self, param_dict):
        for unit in self:
            if unit.module:
                unit.module.init_param(param_dict)

    def config_param(self, freq):
        for unit in self:
            if unit.module:
                unit.module.config_param(freq)
