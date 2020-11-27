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

    def get_all_nodes(self):
        from src.CircuitConcept.NodeGroup import NodeSet
        tmp = NodeSet()
        for edge in self:
            tmp.add(edge.start)
            tmp.add(edge.end)
        return tmp

    def get_all_var(self):
        from src.CircuitConcept.VariableGroup import VarSet
        tmp = VarSet()
        for obj in self:
            tmp.add(obj.variable)
        return tmp

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names

    def get_connected_graph(self):
        tmp = EdgeList(self)
        return tmp.get_connected_graph()

    def init_gnd(self):
        tmp = EdgeList(self)
        return tmp.init_gnd()


class EdgeList(list):
    """
        边列表
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

    def get_all_nodes(self):
        from src.CircuitConcept.NodeGroup import NodeSet
        tmp = NodeSet()
        for edge in self:
            tmp.add(edge.start)
            tmp.add(edge.end)
        return tmp

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for edge in self:
            names.append(edge.name)
        names.sort()
        return names

    def get_connected_graph(self):

        from src.CircuitConcept.NodeGroup import NodeSet
        tmp = list()

        for edge in self:
            f1 = -1
            f2 = -1

            counter = 0
            for ele in tmp:
                if edge.start in ele:
                    f1 = counter
                    break
                counter += 1

            counter = 0
            for ele in tmp:
                if edge.end in ele:
                    f2 = counter
                    break
                counter += 1

            if f1 < 0 and f2 < 0:
                ele = NodeSet()
                ele.add(edge.start)
                ele.add(edge.end)
                tmp.append(ele)
            elif f1 < 0:
                tmp[f2].add(edge.start)
            elif f2 < 0:
                tmp[f1].add(edge.end)
            elif f1 == f2:
                pass
            else:
                tmp[f1].update(tmp[f2])
                tmp.pop(f2)

        return tmp

    def init_gnd(self):
        tmp = self.get_connected_graph()
        for obj in tmp:
            obj.init_gnd()
