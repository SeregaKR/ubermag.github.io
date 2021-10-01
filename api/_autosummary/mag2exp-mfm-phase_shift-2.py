# 2. Visualising in-plane MFM with ``matplotlib``.

import discretisedfield as df
import micromagneticmodel as mm
import mag2exp
mesh = df.Mesh(p1=(-25e-9, -25e-9, -2e-9),
               p2=(25e-9, 25e-9, 50e-9),
               cell=(1e-9, 1e-9, 2e-9))
def v_fun(point):
    x, y, z = point
    if x < -2e-9:
        return (0, 0, 1)
    elif x < 2e-9:
        return (0, 1, 0)
    else:
        return (0, 0, -1)
def Ms_fun(pos):
    x, y, z = pos
    if (z < 0):
        return 384e3
    else:
        return 0
system = mm.System(name='Box2')
system.energy = mm.Demag()
system.m = df.Field(mesh, dim=3, value=v_fun, norm=Ms_fun)
ps = mag2exp.mfm.phase_shift(system, tip_m=(1e-16, 0, 0))
# Running OOMMF...
ps.plane(z=10e-9).mpl.scalar()
ps.plane(z=40e-9).mpl.scalar()
