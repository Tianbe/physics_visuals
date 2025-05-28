import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

# plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.rcParams["mathtext.fontset"] = "cm"

fig, ax = plt.subplots(figsize=(6, 4))
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.axes.set_frame_on(False)

# shape = (121, 81)
shape = (61, 41)
aspect_ratio = shape[0] / shape[1]
length = 6 * np.pi

x_val0 = np.linspace(0, length, shape[0])
y_val0 = np.linspace(0, length / aspect_ratio, shape[1])

x_coords0, y_coords0 = np.meshgrid(x_val0, y_val0)

x_coords0_update = 0.6 * np.sin(x_coords0)

x_final = x_coords0 + x_coords0_update

h_lines_0 = x_coords0.T#[::2]
h_lines_def = x_final.T#[::2]
v_lines = y_coords0#[::2]

# ax.set_box_aspect(1/aspect_ratio)
ax.set_ylim(-2, y_val0.max() + 2)
ax.set_xlim(-0.2, length + 0.2)
ax.set_adjustable("datalim")

for v_line in v_lines:
    # v_line_spl = make_smoothing_spline(x_val0, v_line, lam=1)
    ax.plot(x_val0, v_line, color="k", alpha=0.6, lw=1)
for h_line in h_lines_def:
    # h_line_spl = make_smoothing_spline(y_val0, h_line, lam=1)
    ax.plot(h_line, y_val0, color="k", alpha=0.6, lw=1)

plt.annotate(
    "",
    xy=(np.pi * 3, -0.5),
    xytext=(np.pi, -0.5),
    # arrowprops=dict(arrowstyle=patches.ArrowStyle('CurveFilledAB'))
    arrowprops=dict(
        arrowstyle=patches.ArrowStyle(
            "<|-|>", head_length=0.5, head_width=0.2, widthA=1.5, widthB=1.5
        )
    ),
)
plt.text(np.pi * 2, -1.5, r"$\Lambda$", fontsize=16, ha="center")

plt.annotate(
    "",
    xy=(np.pi * 2, y_coords0.max() + 0.5),
    xytext=(np.pi * 4, y_coords0.max() + 0.5),
    arrowprops=dict(
        arrowstyle=patches.ArrowStyle(
            "<|-", head_length=0.5, head_width=0.2, widthA=1.5, widthB=1.5
        )
    ),
)
plt.text(np.pi * 3, y_coords0.max() + 1, "$k_x$", fontsize=16, ha="center")

fig.savefig(r'C:..\..\plots'
            + r'\long_wave.svg',
            transparent=True)
