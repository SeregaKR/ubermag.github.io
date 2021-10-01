# 1. Visualising the scalar field using ``matplotlib``.

import discretisedfield as df
# ...
p1 = (0, 0, 0)
p2 = (100, 100, 100)
n = (10, 10, 10)
mesh = df.Mesh(p1=p1, p2=p2, n=n)
field = df.Field(mesh, dim=3, value=(1, 2, 3))
# ...
field.plane('z').mpl.lightness()