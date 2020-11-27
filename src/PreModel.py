from src.Parameter import Parameter
from src.TrackCircuitConcept.SectionGroup import SectionGroup
from src.TrackCircuitConcept.Line import Line
from src.TrackCircuitConcept.Line import LineGroup
from src.TrackCircuitConcept.Train import Train

from src.ParamType import CapacitanceType
from src.ParamType import ResistanceType
from src.ParamType import MultiFreqImpType

from src.Equation.EquationGroup import EquationGroup


class PreModel:
    """
        前置模型
    """

    def __init__(self):

        self.main_freq = 1700

        pd = Parameter.read_param_pkl()

        self.pd = pd

        pd['Param_CapC'] = CapacitanceType(25e-6)
        pd['Param_R_Short'] = ResistanceType(10e-7)
        # pd['Param_R_Short'] = ResistanceType(0)
        pd['Param_Rd'] = ResistanceType(10000)

        tmp = MultiFreqImpType()
        tmp.rlc_s = {
            1700: [1.177, 1.314e-3, None],
            2000: [1.306, 1.304e-3, None],
            2300: [1.435, 1.297e-3, None],
            2600: [1.558, 1.291e-3, None],
        }
        pd['Param_Z_Track'] = tmp

        self.line1 = Line(parent=None, bas_name='线路1')
        self.line2 = Line(parent=None, bas_name='线路2')

        self.lg = LineGroup(parent=None, bas_name='test', lines=[self.line1])

        self.sg1 = SectionGroup(
            parent=None,
            bas_name='地面',
            rlt_pos=0,
            m_nbr=1,
            m_freqs=[1700, 2300],
            m_lens=[650, 300],
            j_lens=[0, 0, 29],
            sec_type='2000A',
            c_nbrs=[7, 0],
            sr_mode='左发',
            snd_lvl=1,
            cable_len=10,
            tb_mode='无TB',
        )

        self.sg2 = SectionGroup(
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

        self.train1 = Train(parent=None, bas_name='列车1', rlt_pos=10)

        self.line1.add_element(self.sg1)
        self.line1.add_element(self.train1)
        # self.line2.add_element(self.sg2)

        self.lg.init_unit()
        # self.line1.ele_units.create_module()
        #
        # self.line1.ele_units.init_param(param_dict=pd)
        # self.line1.ele_units.config_param(self.main_freq)

    def create_track_model(self):

        self.line1.ele_units.create_module()

        self.line1.ele_units.init_param(param_dict=self.pd)
        self.line1.ele_units.config_param(self.main_freq)

        self.lg.init_track_nodes()
        self.lg.init_track()
        self.line1.track_units.create_module()

        self.lg.link_track()
        self.line1.track_units.init_param(param_dict=self.pd)
        self.line1.track_units.config_param(self.main_freq)

    def config_param(self, freq):
        self.line1.ele_units.config_param(freq)
        self.line1.track_units.config_param(freq)

    def calculate(self):
        self.create_track_model()

        self.line1.get_all_modules()
        self.line1.get_all_edges().init_gnd()
        self.line1.get_all_nodes()

        eg = EquationGroup()

        eg.get_var(self.line1.get_all_vars())
        eg.get_equations()
        eg.create_matrix()
        eg.solve_matrix()

        print(eg.length)
