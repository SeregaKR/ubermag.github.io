# 1. Visualising unpolarised cross section with ``matplotlib``.

import discretisedfield as df
import micromagneticmodel as mm
import numpy as np
import mag2exp
mesh = df.Mesh(p1=(-25e-9, -25e-9, -2e-9),
               p2=(25e-9, 25e-9, 50e-9),
               cell=(1e-9, 1e-9, 2e-9))
def v_fun(point):
    x, y, z = point
    q = 10e-9
    return (0,
            np.sin(2 * np.pi * x / q),
            np.cos(2 * np.pi * x / q))
field = df.Field(mesh, dim=3, value=v_fun, norm=1e5)
field.plane('z').mpl()
cs = mag2exp.sans.cross_section(field, method='unpol',
                                polarisation=(0, 0, 1))
cs.plane(z=0).real.mpl.scalar()
