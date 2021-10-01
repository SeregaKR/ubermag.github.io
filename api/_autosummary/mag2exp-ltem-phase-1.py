# 2. Visualising the phase using ``matplotlib``.

import discretisedfield as df
import mag2exp
mesh = df.Mesh(p1=(-5, -4, -1), p2=(5, 4, 1), cell=(2, 1, 0.5))
# ...
def value_fun(point):
    x, y, z = point
    if x > 0:
        return (0, -1, 0)
    else:
        return (0, 1, 0)
# ...
field = df.Field(mesh, dim=3, value=value_fun)
phase, ft_phase = mag2exp.ltem.phase(field)
phase.mpl.scalar()
