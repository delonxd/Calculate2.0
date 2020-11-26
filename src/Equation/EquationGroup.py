class EquationGroup:
    """
        方程组
    """

    def __init__(self):
        self.src_dict = dict()
        self.var_dict = dict()

        # self.length

        self.equations = list()
        self.coeff_list = list()

    def get_var(self, var_set):
        self.var_dict.clear()
        for index, var in enumerate(var_set):
            self.var_dict[var] = index
        return self.var_dict

    @property
    def length(self):
        return len(self.var_dict)

    def get_equations(self):
        self.equations.clear()
        for var in self.var_dict:
            self.equations.append(var.get_equation(self))
        return self.equations
