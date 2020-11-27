class Equation:
    """
        方程
    """

    def __init__(self):
        self.constant = 0
        self.coeff_list = list()

    def append_coeff(self, var, coeff):
        self.coeff_list.append((var, coeff))

    def clear(self):
        self.constant = 0
        self.coeff_list = list()

    @property
    def names(self):
        tmp = list()
        for var, coeff in self.coeff_list:
            tmp.append((var.name, coeff))
        return tmp


if __name__ == '__main__':
    a = Equation()
    a.append_coeff(4, 1.34)
    pass
