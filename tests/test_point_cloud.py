"""
A Python module for radar simulation

----------
RadarSimPy - A Radar Simulator Built with Python
Copyright (C) 2018 - PRESENT  radarsimx.com
E-mail: info@radarsimx.com
Website: https://radarsimx.com

"""

import numpy as np
import numpy.testing as npt
from radarsimpy.rt import lidar_scene


def test_lidar():
    ground = {
        "model": "./models/surface_60x60.stl",
        "location": (0, 0, 0),
        "rotation_axis": (0, 0, 0),
        "rotation_angle": 0,
        "speed": (0, 0, 0),
    }

    targets = [ground]

    lidar = {
        "position": [0, 0, 1.5],
        "phi": np.arange(0, 360, 60),
        "theta": np.array([110, 120]),
    }

    points = lidar_scene(lidar, targets)

    npt.assert_almost_equal(
        points["positions"],
        np.array(
            [
                [4.1212144e00, 0.0000000e00, 1.1920929e-07],
                [2.5980759e00, 0.0000000e00, 1.1920929e-07],
                [2.0606072e00, 3.5690768e00, 1.1920929e-07],
                [1.2990378e00, 2.2499995e00, 1.1920929e-07],
                [-2.0606077e00, 3.5690765e00, 1.1920929e-07],
                [-1.2990381e00, 2.2499995e00, 1.1920929e-07],
                [-4.1212144e00, -3.6028803e-07, 1.1920929e-07],
                [-2.5980759e00, -2.2713100e-07, 1.1920929e-07],
                [-2.0606070e00, -3.5690768e00, 1.1920929e-07],
                [-1.2990375e00, -2.2499995e00, 1.1920929e-07],
                [2.0606070e00, -3.5690768e00, 1.1920929e-07],
                [1.2990375e00, -2.2499995e00, 1.1920929e-07],
            ]
        ),
        decimal=3,
    )

    npt.assert_almost_equal(
        points["directions"],
        np.array(
            [
                [9.3969262e-01, 0.0000000e00, 3.4202024e-01],
                [8.6602539e-01, 0.0000000e00, 5.0000006e-01],
                [4.6984628e-01, 8.1379771e-01, 3.4202024e-01],
                [4.3301266e-01, 7.5000000e-01, 5.0000006e-01],
                [-4.6984637e-01, 8.1379765e-01, 3.4202024e-01],
                [-4.3301275e-01, 7.5000000e-01, 5.0000006e-01],
                [-9.3969262e-01, -8.2150535e-08, 3.4202024e-01],
                [-8.6602539e-01, -7.5710346e-08, 5.0000006e-01],
                [-4.6984622e-01, -8.1379771e-01, 3.4202024e-01],
                [-4.3301257e-01, -7.5000000e-01, 5.0000006e-01],
                [4.6984622e-01, -8.1379771e-01, 3.4202024e-01],
                [4.3301257e-01, -7.5000000e-01, 5.0000006e-01],
            ]
        ),
        decimal=3,
    )
    print(points)
