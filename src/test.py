from src.Parameter import Parameter
from src.TrackCircuitConcept.SectionGroup import SectionGroup
from src.TrackCircuitConcept.Line import Line
from src.TrackCircuitConcept.Line import LineGroup
from src.TrackCircuitConcept.Train import Train
from src.Freq import Freq
from src.ParamType import CapacitanceType
from src.ParamType import ResistanceType
from src.ParamType import MultiFreqImpType
# from src.Unit.BasicUnit import UnitGroup
from src.Unit.UnitGroup import UnitGroup
import os
import sys


if __name__ == '__main__':
    pd = Parameter.read_param_pkl()
    pd['Param_CapC'] = CapacitanceType(25e-6)
    pd['Param_R_Short'] = ResistanceType(10e-7)
    pd['Param_Rd'] = ResistanceType(1)
    tmp = MultiFreqImpType()
    tmp.rlc_s = {
        1700: [1.177, 1.314e-3, None],
        2000: [1.306, 1.304e-3, None],
        2300: [1.435, 1.297e-3, None],
        2600: [1.558, 1.291e-3, None],
    }
    pd['Param_Z_Track'] = tmp

    a = Parameter.read_param_pkl()
    # a = Parameter.read_param_lib()

    sg1 = SectionGroup(
        parent=None,
        bas_name='地面',
        rlt_pos=30,
        m_nbr=1,
        m_freqs=[1700, 2300],
        m_lens=[650, 300],
        j_lens=[0, 0, 29],
        sec_type='2000A',
        c_nbrs=[7, 0],
        sr_mode='左发',
        snd_lvl=1,
        cable_len=10,
        tb_mode='双端TB',
        # parameter=parameter,
    )

    sg2 = SectionGroup(
        parent=None,
        bas_name='地面',
        rlt_pos=30,
        m_nbr=1,
        m_freqs=[2300, 1700],
        m_lens=[650, 300],
        j_lens=[20, 50, 29],
        sec_type='2000A',
        c_nbrs=[3, 0],
        sr_mode='左发',
        snd_lvl=1,
        cable_len=10,
        tb_mode='双端TB',
        # parameter=parameter,
    )

    # xx = sg1.sec_list[1].l_tcsr
    # ug1 = UnitGroup(sg1.get_all_units())
    # yy = ug1.get_unit_pos()
    # zz = ug1.get_name_list()
    # ug1.create_module()

    t1 = Train(parent=None, bas_name='列车1')

    l1 = Line(parent=None, bas_name='线路1')

    l1.add_element(sg1)
    l1.add_element(t1)

    l2 = Line(parent=None, bas_name='线路2')
    l2.add_element(sg2)

    lg1 = LineGroup(parent=None, bas_name='test', lines=[l1])

    lg1.init_unit()

    ug1 = lg1.ele_units
    pos = ug1.pos_set
    names = ug1.name_list

    ug1.create_module()
    ug1.init_param(param_dict=pd)
    ug1.config_param(1700)

    # l1.init_track()
    lg1.init_track_nodes()
    lg1.init_track()

    tu = l1.track_units
    tu.create_module()
    tu.init_param(param_dict=pd)
    tu.config_param(1700)


    pass