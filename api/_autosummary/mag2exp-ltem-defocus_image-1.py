# 2. Visualising the phase using ``matplotlib``.

import discretisedfield as df
import mag2exp
mesh = df.Mesh(p1=(-5e-9, -4e-9, -1e-9), p2=(5e-9, 4e-9, 1e-9),
                   cell=(2e-9, 1e-9, 0.5e-9))
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
df_img = mag2exp.ltem.defocus_image(phase, cs=8000,
                                    df_length=0.2e-3,
                                    voltage=300e3)
df_img.mpl.scalar()
