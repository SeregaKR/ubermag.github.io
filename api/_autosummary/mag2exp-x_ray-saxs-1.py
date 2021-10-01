# 1. Visualising the scattering with ``matplotlib``.

import discretisedfield as df
import numpy as np
import mag2exp
mesh = df.Mesh(p1=(0, 0, 0), p2=(50e-9, 50e-9, 1e-9),
               cell=(1e-9, 1e-9, 1e-9))
def value_fun(point):
    x, y, z = point
    qx = 10e-9
    return (np.sin(2 * np.pi * x/ qx),
            0,
            np.cos(2 * np.pi * x/ qx))
field = df.Field(mesh, dim=3, value=value_fun, norm=0.3e6)
xrs = mag2exp.x_ray.saxs(field)
xrs.mpl.scalar()
