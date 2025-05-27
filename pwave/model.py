import numpy as np


def travelling_sin_wave(x, amplitude=0.6, k=1, w=1.0, t=0.0):
    return amplitude * np.sin(k * x - w * t)


def travelling_radial_wave(x, y, amplitude=0.6, k=1, w=1.0, t=0.0):
    x0, y0 = np.mean(x), np.mean(y)
    r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    r_update = amplitude * np.sin(k * r - w * t)
    alpha = np.arcsin(x / r)
    return np.sin(alpha) * r_update, np.cos(alpha) * r_update


def standing_wave(x, amplitude=0.6, k=1.0, w=1.0, t=0.0):
    return amplitude * np.sin(k * x) * np.cos(w * t)


class ParticleField:
    def __init__(
        self,
        shape=(51, 41),
        x_max=4 * np.pi,
        seed=42,
    ):
        self._rng = np.random.default_rng(seed=seed)
        self.shape = shape

        self.aspect_ratio = self.shape[0] / self.shape[1]
        self.x0_max = x_max
        self.y0_max = self.x0_max / self.aspect_ratio

        self.x0_range = np.linspace(0, self.x0_max, self.shape[0])
        self.y0_range = np.linspace(0, self.y0_max, self.shape[1])
        self.x, self.y = np.meshgrid(self.x0_range, self.y0_range)

        self.x_flat = np.reshape(self.x, -1)
        self.y_flat = np.reshape(self.y, -1)

    def _update_coords(self, x=None, y=None):
        if np.any(x):
            self.x = x
            self.x_flat = np.reshape(self.x, -1)
        if np.any(y):
            self.y = y
            self.y_flat = np.reshape(self.y, -1)

    def apply_noise(self, noise_level=0.24):
        x_noise = self._rng.random(self.shape).T * noise_level - noise_level / 2
        y_noise = self._rng.random(self.shape).T * noise_level - noise_level / 2
        self._update_coords(self.x + x_noise, self.y + y_noise)

    def apply_wave(self, **wave_kwargs):
        x_pressure = travelling_sin_wave(self.x, **wave_kwargs)
        self._update_coords(self.x + x_pressure)
