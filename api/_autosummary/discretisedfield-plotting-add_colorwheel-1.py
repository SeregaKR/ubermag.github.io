# 1. Adding a colorwheel to an empty axis
import discretisedfield.plotting as dfp
import matplotlib.pyplot as plt
# ...
fig, ax = plt.subplots()
ins_ax = dfp.add_colorwheel(ax)
