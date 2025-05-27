import matplotlib.pyplot as plt
import numpy as np

from plot_styles import set_plot_style

from pwave.model import ParticleField
from pwave.animation import PWaveAnim

set_plot_style("large_style")
plt.rcParams["mathtext.fontset"] = "cm"


pf = ParticleField(shape=(55, 25), x_max=4 * np.pi)

fig, ax = plt.subplots(figsize=(5.5, 2.5))

ax.set_box_aspect(1 / pf.aspect_ratio)

y_val0_max = pf.x0_max / pf.aspect_ratio
ax.set_ylim(-0.2, y_val0_max + 0.2)
ax.set_xlim(-0.2, pf.x0_max + 0.2)


ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.spines[["right", "left", "top", "bottom"]].set_visible(False)

plt_kwargs = {
    "color": (0.14, 0.14, 0.3),
    "marker": "o",
    "s": 18,
    "alpha": 0.24,
    "lw": 0,
}
pws = PWaveAnim(pf, np.linspace(0.0, 8 * np.pi, 200), figure=fig, plt_kwargs=plt_kwargs)
plt.show()


pws.ani.save(r'..\..\plots' + '\pwave4pi.gif')

# import imageio
#
# # Load the full animation
# full_gif = imageio.mimread(r'..\..\plots' + 'physics_visuals.gif')
#
# # Select every 5th frame
# subset_gif = full_gif[1:]  # Keep every 5th frame
#
# # Save the new subset GIF
# imageio.mimsave(r'..\..\plots' + 'pwave_crop.gif', subset_gif, fps=20)
