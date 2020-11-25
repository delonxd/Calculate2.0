import numpy as np


class Rail:
    """
        钢轨
    """

    def __init__(self):
        self._l_pos = -np.inf
        self._r_pos = np.inf
        self._param = None

    @property
    def l_pos(self):
        return self._l_pos

    @property
    def r_pos(self):
        return self._r_pos

    @property
    def z_trk(self):
        return

    @property
    def rd(self):
        return


class RailGroup:
    """
        钢轨组
    """

    def __init__(self):
        self.rails = set()

    def add_rail(self, new_rail):
        """

        """

        if isinstance(new_rail, Rail):
            new_l = new_rail.l_pos
            new_r = new_rail.r_pos
            for rail in self.rails:
                l_pos = rail.l_pos
                r_pos = rail.r_pos
                if r_pos <= new_l or new_r <= l_pos:
                    pass
                elif l_pos < new_l < r_pos <= new_r:
                    rail.r_pos = new_l
                elif l_pos < new_l < new_r < r_pos:
                    rail.r_pos = new_l
                    tmp = Rail()
                    tmp.l_pos = new_r
                    tmp.r_pos = r_pos
                    self.rails.add(tmp)
                elif new_l <= l_pos < new_r < r_pos:
                    rail.l_pos = new_r
                elif new_l <= l_pos < r_pos <= new_r:
                    self.rails.discard(rail)
            # new_rail.parant_line = self.parent_ins
            self.rails.add(new_rail)
