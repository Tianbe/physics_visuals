import numpy as np
from pwave.molecules import ParticleSubGroup
from pwave.model import ParticleField


def test_particles_one_dim():
    x = np.arange(20)
    all = ParticleSubGroup(x, x)
    r = all.pop_rd_group()
    print(r.x, r.y)
    for x_i, y_i in zip(r.x, r.y):
        assert x_i not in all.x
        assert y_i not in all.y


def test_particle_field_pop():
    shape = (5, 3)
    aspect_ratio = shape[0] / shape[1]
    x_max = 4
    p1 = ParticleField(shape=shape, x_max=x_max)
    particles = ParticleSubGroup(p1.x_flat, p1.y_flat)
    b_particles = particles.pop_rd_group(0.2)
    all_x = np.sort(particles.x + b_particles.x)
    all_y = np.sort(particles.y + b_particles.y)
    # for x_i, y_i in zip(r.x, r.y):
    all_x_test, all_y_test = np.meshgrid(
        np.linspace(0, x_max, shape[0]), np.linspace(0, x_max / aspect_ratio, shape[1])
    )

    assert np.array_equal(all_x, np.sort(np.reshape(all_x_test, -1)))
    assert np.array_equal(all_y, np.sort(np.reshape(all_y_test, -1)))
