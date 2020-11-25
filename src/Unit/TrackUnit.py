from src.Unit.BasicUnit import BasicUnit
from src.Module.TrackModule import TrackModule


class TrackUnit(BasicUnit):
    """
        钢轨单元
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name

        self._l_pos = None
        self._r_pos = None
        self._mode = None

    @property
    def rlt_pos(self):
        if self._rlt_pos is None:
            return 0
        else:
            return self._rlt_pos

    @property
    def abs_pos(self):
        return self.rlt_pos

    @property
    def bas_name(self):
        if self._bas_name is None:
            return ''
        else:
            return self._bas_name

    @property
    def name(self):
        if self.parent is None:
            return self.bas_name
        else:
            name = self.parent.name + '_' + self.bas_name
            self._name = name
            return name

    def load_kwargs(self, **kwargs):

        if 'bas_name' in kwargs:
            self._bas_name = kwargs['bas_name']

        if 'l_pos' in kwargs:
            self._l_pos = kwargs['l_pos']

        if 'r_pos' in kwargs:
            self._r_pos = kwargs['r_pos']

        if 'mode' in kwargs:
            self._mode = kwargs['mode']
