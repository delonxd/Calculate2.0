class Variable:
    """
        变量
    """

    def __init__(self, parent):
        self.parent = parent
        self._name = str()

    def get_equation(self, equs):
        print(self.name)
        return self.parent.get_equation(equs)

    @property
    def name(self):
        return


class VoltageVar(Variable):
    """
        电压变量
    """

    def __init__(self, parent):
        super().__init__(parent)

    @property
    def name(self):
        name = self.parent.name + '_电压'
        self._name = name
        return name


class CurrentVar(Variable):
    """
        电流变量
    """

    def __init__(self, parent):
        super().__init__(parent)

    @property
    def name(self):
        name = self.parent.name + '_电流'
        self._name = name
        return name


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
