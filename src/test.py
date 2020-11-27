from src.PreModel import PreModel


def vol_abs(obj1, obj2):
    return abs(obj1.voltage - obj2.voltage)


if __name__ == '__main__':

    md = PreModel()
    md.train1.load_kwargs(rlt_pos=350)
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

        print('%f0.5' % i_short)
        print('%f0.5' % v_short)
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
    pass