import matplotlib
import matplotlib.animation as animation
import numpy as np

from pwave.model import ParticleField, travelling_sin_wave

matplotlib.use("TkAgg")



class PWaveAnim:

    def __init__(self, pf: ParticleField, t_range, figure, plt_kwargs: dict):
        self.pf = pf
        self.t_range = t_range
        self.frames = []
        self.fig = figure
        self.ax = figure.gca()
        self.plt_kwargs = plt_kwargs
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update,
            interval=40,
            repeat_delay=0,
            frames=len(t_range) - 1,
            init_func=self.setup_plot,
            blit=False,
            repeat=False,
        )

    def _periodic_boundary(self):
        # indexes out of upper boundary
        ix_up_out = np.where(self.pf.x_flat > self.pf.x0_max)
        iy_up_out = np.where(self.pf.y_flat > self.pf.y0_max)
        # indexes out of lower boundary
        ix_low_out = np.where(self.pf.x_flat < self.pf.x0_range.min())
        iy_low_out = np.where(self.pf.y_flat < self.pf.y0_range.min())
        # shift back into boundaries
        self.pf.x_flat[ix_up_out] = self.pf.x_flat[ix_up_out] - self.pf.x0_max
        self.pf.y_flat[iy_up_out] = self.pf.y_flat[iy_up_out] - self.pf.y0_max

        self.pf.x_flat[ix_low_out] = self.pf.x_flat[ix_low_out] + self.pf.x0_max
        self.pf.y_flat[iy_low_out] = self.pf.y_flat[iy_low_out] + self.pf.y0_max
        # todo: only flat indicees are updated so far

    def wave_step(self, i, **wave_kwargs):
        x_sin = travelling_sin_wave(
            self.pf.x_flat, amplitude=0.8, t=self.t_range[i + 1], **wave_kwargs
        )
        return x_sin

    def setup_plot(self):
        self.scat = self.ax.scatter(self.pf.x_flat, self.pf.y_flat, **self.plt_kwargs)
        self.pf.apply_noise(0.4)
        self._periodic_boundary()
        self.update(-1)
        return []

    def update(self, i):
        self.ax.clear()

        y_val0_max = self.pf.x0_max / self.pf.aspect_ratio
        self.ax.set_ylim(-0.2, y_val0_max + 0.2)
        self.ax.set_xlim(-0.2, self.pf.x0_max + 0.2)

        # todo: implement flexible noise level
        self.pf.apply_noise(0.08)
        x_shift = self.wave_step(i)
        self._periodic_boundary()
        self.scat = self.ax.scatter(
            self.pf.x_flat + x_shift, self.pf.y_flat, **self.plt_kwargs
        )
        return []
