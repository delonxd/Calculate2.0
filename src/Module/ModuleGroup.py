from src.Module.BasicModule import BasicModule


class ModuleSet(set):
    """
        模块集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_list = list()

    def add(self, obj):
        if isinstance(obj, BasicModule):
            super().add(obj)
        else:
            raise KeyboardInterrupt("%s应为BasicModule类型" % obj)

    def update(self, obj):
        if isinstance(obj, ModuleSet):
            super().update(obj)
        else:
            raise KeyboardInterrupt("%s应为ModuleSet类型" % obj)

    def init_param(self, param_dict):
        for module in self:
            module.init_param(param_dict)

    def config_param(self, freq):
        for module in self:
            module.config_param(freq)

    def get_all_edges(self):
        from src.CircuitConcept.EdgeGroup import EdgeSet
        tmp = EdgeSet()

        for module in self:
            tmp.update(module.get_all_edges())
        return tmp

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names


class ModuleList(list):
    """
        模块列表
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_list = list()

    def append(self, obj):
        if isinstance(obj, BasicModule):
            super().append(obj)
        else:
            raise KeyboardInterrupt("%s应为BasicModule类型" % obj)

    def extend(self, obj):
        if isinstance(obj, ModuleList):
            super().extend(obj)
        else:
            raise KeyboardInterrupt("%s应为ModuleList类型" % obj)

    def init_param(self, param_dict):
        for module in self:
            module.init_param(param_dict)

    def config_param(self, freq):
        for module in self:
            module.config_param(freq)

    def get_all_edges(self):
        from src.CircuitConcept.EdgeGroup import EdgeSet
        tmp = EdgeSet()

        for module in self:
            tmp.update(module.get_all_edges())
        return tmp

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names
