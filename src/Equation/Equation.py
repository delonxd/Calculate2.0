import numpy as np


class Equation:
    """
        方程
    """

    def __init__(self, length):
        self.constant = 0
        self.coeff_list = np.zeros(length, dtype=complex)

    def config_coeff(self, column, value):
        self.coeff_list[column] = value


if __name__ == '__main__':
    a = Equation(5)
    a.config_coeff(4, 1.34)

    pass