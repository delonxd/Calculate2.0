from src.CircuitConcept.Edge import Edge


class EdgeSet(set):
    """
        边集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_list = list()

    def add(self, obj):
        if isinstance(obj, Edge):
            super().add(obj)
        else:
            raise KeyboardInterrupt("%s应为Edge类型" % obj)

    def update(self, obj):
        if isinstance(obj, EdgeSet):
            super().update(obj)
        else:
            raise KeyboardInterrupt("%s应为EdgeSet类型" % obj)

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names


class EdgeList(list):
    """
        模块列表
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_list = list()

    def append(self, obj):
        if isinstance(obj, Edge):
            super().append(obj)
        else:
            raise KeyboardInterrupt("%s应为Edge类型" % obj)

    def extend(self, obj):
        if isinstance(obj, EdgeList):
            super().extend(obj)
        else:
            raise KeyboardInterrupt("%s应为EdgeList类型" % obj)

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names
