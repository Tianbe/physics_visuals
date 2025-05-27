import numpy as np

from pwave.math import calc_distance


class Chain:

    def __init__(
        self,
        c_len,
        x_,
        y_,
        x0=None,
        y0=None,
        smooth=True,
        next_neighbour_lever=1,
        seed=42,
    ):
        self.c_len = c_len
        # x_ and y_ must have the same shape
        # convert to array to allow array indexing e.g., a[1,2,3]
        self.x_ = np.array(x_)
        self.y_ = np.array(y_)
        self.shape = np.shape(self.x_)
        self.seed = seed

        self.x0 = x0
        self.y0 = y0
        if not x0:
            self.x0 = self._pick_random_point()[0]
        if not y0:
            self.y0 = self._pick_random_point()[1]

        self.smooth = smooth
        # int number >= 1; 1: nearest neighbour, 2: second next neighbour, etc
        self.next_neighbour_level = next_neighbour_lever
        self.line_knot_coords = None
        self.line_coords = None

        self._define_line()

    def _pick_random_point(self):
        rng = np.random.default_rng(seed=self.seed)
        idxx = int(rng.random() * self.shape[0])
        idxy = int(rng.random() * self.shape[0])
        return self.x_[idxx], self.y_[idxy]

    def _calc_dist(self):
        return calc_distance(self.x_, self.y_, self.x0, self.y0)

    def _define_line(self):
        # take coordinates of the nearest neighbours
        dist = self._calc_dist()
        line_coord_ind = np.argsort(dist, axis=None)[:: self.next_neighbour_level]
        # x_line_coords = np.take_along_axis(self.x_,
        #                                    line_coord_ind[:self.c_len],
        #                                    axis=None)
        # y_line_coords = np.take_along_axis(self.y_,
        #                                    line_coord_ind[:self.c_len],
        #                                    axis=None)
        x_line_coords = self.x_[line_coord_ind[: self.c_len]]
        y_line_coords = self.y_[line_coord_ind[: self.c_len]]
        x_line_coords.sort()
        self.line_knot_coords = (x_line_coords, y_line_coords)

        if self.smooth:
            # pp = CubicSpline(x_line_coords, y_line_coords, bc_type='clamped')
            x_line_coords_intp = np.linspace(
                x_line_coords.min(), x_line_coords.max(), 100
            )
            params = np.polyfit(x_line_coords, y_line_coords, 4)
            polynom = np.poly1d(params)
            y_line_coords_intp = polynom(x_line_coords_intp)
            self.line_coords = (x_line_coords_intp, y_line_coords_intp)
        else:
            self.line_coords = self.line_knot_coords

    def _find_next_neighbour(self):
        """
        put a function here that similar to _define line,
        but always looks for the nearest neighbour for a given point
        :return:
        """
        pass

    def draw(self, ax, l_kwargs=None, s_kwargs=None):
        if s_kwargs is None:
            s_kwargs = {"color": "g", "alpha": 0.25, "s": 18}
        if l_kwargs is None:
            l_kwargs = {"color": "g", "alpha": 0.8, "lw": 1.5}

        ax.plot(*self.line_coords, **l_kwargs)
        ax.scatter(*self.line_knot_coords, **s_kwargs)


class ParticleSubGroup:
    """This class represents a group of particles that are represented by 2D
    coordinates"""

    def __init__(self, x, y, seed=42):
        self.x = list(x)
        self.y = list(y)
        self.len = len(x)
        self._rng = np.random.default_rng(seed=seed)

    def pop_rd_group(self, fraction=0.1):
        """
        Take a random sample with a given fraction from all particles and remove
        them from the ParticleGroup
        :param fraction: size of particel fraction
        :return: A new particle group
        """
        ind_ar_x = np.arange(self.len)
        # ind_ar_y = np.arange(self.ly)
        sub_id = self._rng.choice(ind_ar_x, int(self.len * fraction), replace=False)
        # y_sub_id = self._rng.choice(ind_ar_y, int(self.ly * fraction), replace=False)
        sub_id_s = sorted(sub_id, reverse=True)
        # y_sub_id_s = sorted(y_sub_id, reverse=True)

        poped_particles = ParticleSubGroup(
            np.array(self.x)[sub_id_s], np.array(self.y)[sub_id_s]
        )

        [self.x.pop(i) for i in sub_id_s]
        [self.y.pop(i) for i in sub_id_s]
        self.len = len(self.x)
        return poped_particles
