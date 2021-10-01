# 1. Visualising the scalar field using ``matplotlib``.

import discretisedfield as df
import math
# ...
p1 = (0, 0, 0)
p2 = (100, 100, 100)
n = (10, 10, 10)
mesh = df.Mesh(p1=p1, p2=p2, n=n)
def init_value(point):
    x, y, z = point
    return math.sin(x) + math.sin(y)
field = df.Field(mesh, dim=1, value=init_value)
# ...
field.plane('z').mpl.contour()
