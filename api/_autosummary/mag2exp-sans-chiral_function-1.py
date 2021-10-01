# 1. Visualising the chiral function with ``matplotlib``.

import discretisedfield as df
import micromagneticmodel as mm
import numpy as np
import mag2exp
mesh = df.Mesh(p1=(-25e-9, -25e-9, -25e-9),
               p2=(25e-9, 25e-9, 25e-9),
               cell=(1e-9, 1e-9, 1e-9))
def v_fun(point):
    x, y, z = point
    q = 10e-9
    return (0,
            np.sin(2 * np.pi * x / q),
            np.cos(2 * np.pi * x / q))
field = df.Field(mesh, dim=3, value=v_fun, norm=1e5)
field.plane('z').mpl()
cf = mag2exp.sans.chiral_function(field,
                                  polarisation=(1, 0, 0))
cf.plane(z=0).mpl.scalar()
