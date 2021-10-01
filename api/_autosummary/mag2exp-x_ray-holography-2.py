# 1. Visualising X-ray holography with ``matplotlib``.

import discretisedfield as df
import mag2exp
mesh = df.Mesh(p1=(-5e-9, -4e-9, 0), p2=(5e-9, 4e-9, 2e-9),
               cell=(1e-9, 1e-9, 1e-9))
def value_fun(point):
    x, y, z = point
    if x < -2e-9:
        return (0, 0, 1)
    elif x < 2e-9:
        return (0, 1, 0)
    else:
        return (0, 0, -1)
field = df.Field(mesh, dim=3, value=value_fun, norm=0.3e6)
xrh2 = mag2exp.x_ray.holography(field, fwhm=(2e-9,2e-9))
xrh2.mpl.scalar()
