from turtle import color
from matplotlib.patches import bbox_artist
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()
# c to tell which values to use as color map, cmap to set a shade (e.g. Blues)
ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=10) # type:ignore 
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(labelsize=14)
# intervallo per ciascun asse
ax.axis((0, 1100, 0, 1_100_000))
ax.ticklabel_format(style="plain")
# show the graph
plt.show()
# save the image as a file, filename, remove white spaces around image
# plt.savefig("squares_plot.png", bbox_inches="tight")



