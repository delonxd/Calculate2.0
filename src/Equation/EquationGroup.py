from src.CircuitConcept.VariableGroup import VarList
import numpy as np


class EquationGroup:
    """
        方程组
    """

    def __init__(self):
        self.vars = VarList()
        self.equations = list()

        self._matrix = None
        self._constant = None

    def get_var(self, var_set):
        self.vars.clear()
        self.vars.extend(var_set)
        return self.vars

    @property
    def length(self):
        return len(self.vars)

    def get_equations(self):
        self.equations.clear()
        for var in self.vars:
            print(var.name)
            self.equations.append(var.get_equation())
            pass
        return self.equations

    def create_matrix(self):
        len_row = len(self.equations)
        len_column = len(self.vars)
        self.vars.init_dict()

        m_matrix = np.zeros((len_row, len_column), dtype=complex)
        constant = np.zeros((len_row, 1), dtype=complex)

        for row, equ in enumerate(self.equations):
            for var, coeff in equ.coeff_list:
                column = self.vars.var2nbr[var]
                m_matrix[row, column] = coeff
            constant[row] = equ.constant
        self._matrix, self._constant = m_matrix, constant

        return m_matrix, constant

    def solve_matrix(self):
        solution = np.linalg.solve(self._matrix, self._constant)
        for index, value in enumerate(solution):
            self.vars.nbr2var[index].value = value
