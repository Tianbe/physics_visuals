import matplotlib.pyplot as plt
import numpy as np

shape = (3, 3)
noise_level = 0.8
x_val0 = np.linspace(0, 4, shape[0])
y_val0 = np.linspace(0, 4, shape[1])

x_coords0, y_coords0 = np.meshgrid(x_val0, y_val0)

rng = np.random.default_rng(seed=42)

x_noise = rng.random(shape).T * noise_level - noise_level / 2
y_noise = rng.random(shape).T * noise_level - noise_level / 2

x_final = x_coords0 + x_noise
y_final = y_coords0 + y_noise

fig, ax = plt.subplots(figsize=(4, 4))
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.axes.set_frame_on(False)
ax.scatter(x_final, y_final, color=(0.82, 0.8, 0.8), marker="o", s=2000, alpha=0.8)

ax.scatter(x_final, y_final, color=(0.7, 0.7, 0.75), marker="o", s=200)
ax.scatter(x_final, y_final, color=(0.4, 0.4, 0.4), marker="o", s=1)

ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
plt.show()

# fig.savefig(r'..\..\plots' + r'\interactions.pdf',
#              bbox_inches="tight",
#             transparent=True)
