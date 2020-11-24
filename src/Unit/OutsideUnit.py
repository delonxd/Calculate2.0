from src.Unit.BasicUnit import BasicUnit
from src.Module.OutsideModule import ZPW2000A_SVA
from src.Module.OutsideModule import ZPW2000A_CapC
from src.Module.OutsideModule import ZPW2000A_TB


class SVA(BasicUnit):
    """
        室外空心线圈
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name
        self._md_type = ZPW2000A_SVA


class CapC(BasicUnit):
    """
        室外补偿电容
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name
        self._md_type = ZPW2000A_CapC


class TB(BasicUnit):
    """
        室外TB
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name
        self._md_type = ZPW2000A_TB

    @property
    def freq(self):
        return


class UPowerOut(BasicUnit):
    """
        室外电压源
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name


class ROutside(BasicUnit):
    """
        室外电阻
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name


class BreakPoint(BasicUnit):
    """
        钢轨断点
    """

    def __init__(self, parent, bas_name):
        super().__init__(parent)
        self._bas_name = bas_name

    def create_module(self):
        pass