from src.CircuitConcept.Node import Node


class NodeSet(set):
    """
        节点集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pos_set = set()
        self._name_list = list()

    def add(self, obj):
        if isinstance(obj, Node):
            super().add(obj)
        else:
            raise KeyboardInterrupt("%s应为Node类型" % obj)

    def update(self, obj):
        if isinstance(obj, NodeSet):
            super().update(obj)
        else:
            raise KeyboardInterrupt("%s应为NodeSet类型" % obj)

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names

    def get_all_var(self):
        from src.CircuitConcept.VariableGroup import VarSet
        tmp = VarSet()
        for obj in self:
            tmp.add(obj.variable)
        return tmp

    def init_gnd(self):
        for index, obj in enumerate(self):
            if index == 0:
                obj.gnd_flg = True
            else:

                obj.gnd_flg = False
