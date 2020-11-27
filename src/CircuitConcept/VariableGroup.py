from src.CircuitConcept.Variable import Variable


class VarSet(set):
    """
        变量集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name_list = list()

    def add(self, obj):
        if isinstance(obj, Variable):
            super().add(obj)
        else:
            raise KeyboardInterrupt("%s应为Variable类型" % obj)

    def update(self, obj):
        if isinstance(obj, VarSet):
            super().update(obj)
        else:
            raise KeyboardInterrupt("%s应为VarSet类型" % obj)

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for obj in self:
            names.append(obj.name)
        names.sort()
        return names


class VarList(list):
    """
        变量集合
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._nbr2var = dict()
        self._var2nbr = dict()
        self._name_list = list()

    @property
    def nbr2var(self):
        return self._nbr2var

    @property
    def var2nbr(self):
        return self._var2nbr

    def append(self, obj):
        if isinstance(obj, Variable):
            super().append(obj)
        else:
            raise KeyboardInterrupt("%s应为Variable类型" % obj)

    def extend(self, obj):
        if isinstance(obj, (VarSet, VarList)):
            super().extend(obj)
        else:
            raise KeyboardInterrupt("%s应为VarSet或VarList类型" % obj)

    def init_dict(self):
        self._nbr2var.clear()
        self._var2nbr.clear()
        for index, var in enumerate(self):
            self._nbr2var[index] = var
            self._var2nbr[var] = index

    @property
    def name_list(self):
        names = self._name_list
        names.clear()
        for obj in self:
            names.append(obj.name)
        names.sort()
        return names
