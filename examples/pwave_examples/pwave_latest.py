import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from scipy.interpolate import make_smoothing_spline

from plot_styles.set_style import set_plot_style
from pwave.model import ParticleField
from pwave.molecules import ParticleSubGroup  # , Chain

set_plot_style("large_style")
plt.rcParams["mathtext.fontset"] = "cm"

# standard shape (51, 41)
# large shape (71, 35)
pf = ParticleField(shape=(51, 41), x_max=4 * np.pi)
x_flat_0, y_flat_0 = pf.x0_range, pf.y0_range

pf.apply_wave(amplitude=0.8)
pf.apply_noise()

grey_particles = ParticleSubGroup(pf.x_flat, pf.y_flat)

# chain2 = Chain(25, grey_particles.x, grey_particles.y, x0=3*np.pi+1, y0=4)
# chain3 = Chain(25, grey_particles.x, grey_particles.y, x0=0.4*np.pi, y0=3)
# chain4 = Chain(25, grey_particles.x, grey_particles.y, x0=2*np.pi+1, y0=8)
#
# chain5 = Chain(25, grey_particles.x, grey_particles.y, x0=2.5*np.pi-0.71, y0=4)
# chain6 = Chain(25, grey_particles.x, grey_particles.y, x0=np.pi-0.5, y0=7)
# chain7 = Chain(25, grey_particles.x, grey_particles.y, x0=2*np.pi-1, y0=2)
#
# chain8 = Chain(25, grey_particles.x, grey_particles.y, x0=3.5*np.pi, y0=1.5)
# chain1 = Chain(25, grey_particles.x, grey_particles.y, x0=3.6*np.pi, y0=8.5)

blue_particles = grey_particles.pop_rd_group(0.05)

# fig, ax = plt.subplots(figsize=(6.5, 3.5))
fig, ax = plt.subplots(figsize=(4.5, 4.5))
ax.set_box_aspect(1 / pf.aspect_ratio)

y_val0_max = pf.x0_max / pf.aspect_ratio
ax.set_ylim(-0.6, y_val0_max + 0.2)
ax.set_xlim(-0.2, pf.x0_max + 0.2)

"""show label"""
ax.tick_params(
    top=False, bottom=False, left=True, right=False, labelleft=True, labelbottom=True
)

ax.set_xticks([2 * np.pi], [r"$\Lambda$"], fontsize=16)
plt.annotate(
    "",
    xy=(np.pi * 3, -0.5),
    xytext=(np.pi, -0.5),
    arrowprops=dict(
        arrowstyle=patches.ArrowStyle(
            "<->", head_length=0.5, head_width=0.2, widthA=1.5, widthB=1.5
        )
    ),
)
"""without axes"""
# ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.spines[["right", "left", "top", "bottom"]].set_visible(False)

# """show amplitude"""
# ax.spines[['right', 'top', 'bottom']].set_visible(False)
# ax.set_yticks([y_val0_max / 4, y_val0_max / 2, y_val0_max / 4 + y_val0_max / 2],
#               ['', '', ''])
# ax.spines['left'].set_bounds(y_val0_max / 4, y_val0_max / 4 + y_val0_max / 2)
# ax.set_ylabel(r'$p$, $\rho$, $n$', fontsize=16)
#
# """plot wave amplitude"""
# wave_grid_x = np.linspace(0, pf.x0_max, 500)
# ax.plot(wave_grid_x, pf.y0_max / 4 * np.sin(wave_grid_x - np.pi / 2) + pf.y0_max / 2,
#         alpha=0.6,
#         lw=4, color='steelblue')


# standard grey: (0.14, 0.14, 0.14, 0.2)
ax.scatter(
    grey_particles.x,
    grey_particles.y,
    color=(0.14, 0.14, 0.3),
    marker="o",
    s=18,
    alpha=0.24,
    lw=0,
)
# ax.scatter(blue_particles.x, blue_particles.y, color=(0, 0, 0.75), marker='o', s=22,
#            alpha=0.32)
ax.scatter(
    blue_particles.x,
    blue_particles.y,
    color=(0.14, 0.14, 0.3),
    marker="o",
    s=18,
    alpha=0.24,
    lw=0,
)

# """plot meshwork"""
# standard: every 5 particle
h_lines = (pf.x).T[1::4]
v_lines = (pf.y)[::4]
#
# # https://stackoverflow.com/questions/33707162/zigzag-or-wavy-lines-in-matplotlib
# # mpl.rc_context({'path.sketch': (5, 15, 1)})
for v_line in v_lines:
    v_line_spl = make_smoothing_spline(x_flat_0, v_line, lam=1)
    plt.plot(x_flat_0, v_line_spl(x_flat_0), color="green", alpha=0.6, lw=1.5)
for h_line in h_lines:
    h_line_spl = make_smoothing_spline(y_flat_0, h_line, lam=1)
    plt.plot(h_line_spl(y_flat_0), y_flat_0, color="green", alpha=0.6, lw=1.5)

# plt.show()

# chain2.draw(ax)
# chain3.draw(ax)
# chain4.draw(ax)
# chain5.draw(ax)
# chain6.draw(ax)
# chain7.draw(ax)
# chain8.draw(ax)
# chain1.draw(ax)


# fig.savefig(r'C:..\..\plots'
#             + r'\pwave_3chains_2.svg',
#             transparent=True)
