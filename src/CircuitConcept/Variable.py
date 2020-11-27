class Variable:
    """
        变量
    """

    def __init__(self, parent):
        self.parent = parent
        self._name = str()
        self._value = None

    def get_equation(self):
        return self.parent.get_equation()

    @property
    def name(self):
        return

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def value_abs(self):
        return abs(self.value)


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
