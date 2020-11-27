from src.PreModel import PreModel
import pandas as pds
import time


def vol_abs(obj1, obj2):
    return abs(obj1.voltage - obj2.voltage)


if __name__ == '__main__':

    localtime = time.localtime()
    timestamp = time.strftime("%Y%m%d%H%M%S", localtime)
    print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

    md = PreModel()
    md.train1.load_kwargs(rlt_pos=100)
    md.calculate()
    i_short = md.train1.r_short.module.r1.current_abs
    v_short = md.train1.r_short.module.r1.voltage_abs
    tmp = list()
    for pos in range(0, 651, 50):
        # print(pos)
        md.train1.load_kwargs(rlt_pos=pos)
        md.calculate()
        i_short = md.train1.r_short.module.r1.current_abs
        v_short = md.train1.r_short.module.r1.voltage_abs

        print('%.3e' % i_short)
        tmp.append(i_short)
    #
    #     # i_short = md.train1

    sg1 = md.sg1

    md1 = sg1.sec_list[0].l_tcsr.module
    md2 = sg1.sec_list[0].r_tcsr.module

    vpp = vol_abs(md1.power.u1.start, md1.power.u1.end)
    v_power = vol_abs(md1.power.ports[0], md1.power.ports[1])
    v_receiver = vol_abs(md2.receiver.ports[0], md2.receiver.ports[1])

    v1 = vol_abs(md1.power.ports[0], md1.power.ports[1])
    v2 = vol_abs(md1.cable.ports[0], md1.cable.ports[1])
    v3 = vol_abs(md1.cable.ports[2], md1.cable.ports[3])
    v4 = vol_abs(md1.tad_xfmr.ports[2], md1.tad_xfmr.ports[3])
    a = md1.tad_xfmr.ports[2].voltage - md1.tad_xfmr.ports[3].voltage

    df1 = pds.DataFrame(tmp)

    #################################################################################

    # 保存到本地excel

    path = '仿真输出_%s.xlsx' % timestamp
    with pds.ExcelWriter(path) as writer:
        df1.to_excel(writer, sheet_name='result')

    pass