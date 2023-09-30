"""
A Python module for radar simulation

----------
RadarSimPy - A Radar Simulator Built with Python
Copyright (C) 2018 - PRESENT  radarsimx.com
E-mail: info@radarsimx.com
Website: https://radarsimx.com

"""

import radarsimpy.processing as proc
import numpy as np
import numpy.testing as npt

covmat_est = np.array(
    [
        [
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601430 * 1j,
            2.26109130412416 + 0.989143898037957 * 1j,
            -0.378365978640197 + 0.889536536650390 * 1j,
            1.13549289576738 + 0.552382221616346 * 1j,
            -0.990501697296642 - 0.183694849224894 * 1j,
            1.28472431753472 - 0.629797821850576 * 1j,
            -0.136214149861948 - 1.07377729071515 * 1j,
            2.48622500160235 - 0.775783252972922 * 1j,
            0.925034243757439 - 0.501055069082895 * 1j,
            2.96213213022416 + 0.365264316268174 * 1j,
        ],
        [
            0.794230483767640 - 0.595755572601430 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601430 * 1j,
            2.26109130412416 + 0.989143898037955 * 1j,
            -0.378365978640197 + 0.889536536650388 * 1j,
            1.13549289576738 + 0.552382221616346 * 1j,
            -0.990501697296642 - 0.183694849224890 * 1j,
            1.28472431753472 - 0.629797821850576 * 1j,
            -0.136214149861947 - 1.07377729071516 * 1j,
            2.48622500160235 - 0.775783252972922 * 1j,
            0.925034243757439 - 0.501055069082895 * 1j,
        ],
        [
            2.26109130412416 - 0.989143898037957 * 1j,
            0.794230483767640 - 0.595755572601430 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601431 * 1j,
            2.26109130412416 + 0.989143898037957 * 1j,
            -0.378365978640197 + 0.889536536650388 * 1j,
            1.13549289576738 + 0.552382221616343 * 1j,
            -0.990501697296642 - 0.183694849224890 * 1j,
            1.28472431753472 - 0.629797821850573 * 1j,
            -0.136214149861947 - 1.07377729071516 * 1j,
            2.48622500160235 - 0.775783252972922 * 1j,
        ],
        [
            -0.378365978640197 - 0.889536536650390 * 1j,
            2.26109130412416 - 0.989143898037955 * 1j,
            0.794230483767640 - 0.595755572601431 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601428 * 1j,
            2.26109130412416 + 0.989143898037959 * 1j,
            -0.378365978640197 + 0.889536536650390 * 1j,
            1.13549289576738 + 0.552382221616345 * 1j,
            -0.990501697296642 - 0.183694849224896 * 1j,
            1.28472431753472 - 0.629797821850571 * 1j,
            -0.136214149861947 - 1.07377729071516 * 1j,
        ],
        [
            1.13549289576738 - 0.552382221616346 * 1j,
            -0.378365978640197 - 0.889536536650388 * 1j,
            2.26109130412416 - 0.989143898037957 * 1j,
            0.794230483767640 - 0.595755572601428 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601430 * 1j,
            2.26109130412416 + 0.989143898037953 * 1j,
            -0.378365978640197 + 0.889536536650392 * 1j,
            1.13549289576738 + 0.552382221616346 * 1j,
            -0.990501697296642 - 0.183694849224894 * 1j,
            1.28472431753472 - 0.629797821850573 * 1j,
        ],
        [
            -0.990501697296642 + 0.183694849224894 * 1j,
            1.13549289576738 - 0.552382221616346 * 1j,
            -0.378365978640197 - 0.889536536650388 * 1j,
            2.26109130412416 - 0.989143898037959 * 1j,
            0.794230483767640 - 0.595755572601430 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601433 * 1j,
            2.26109130412416 + 0.989143898037953 * 1j,
            -0.378365978640197 + 0.889536536650388 * 1j,
            1.13549289576738 + 0.552382221616346 * 1j,
            -0.990501697296642 - 0.183694849224894 * 1j,
        ],
        [
            1.28472431753472 + 0.629797821850576 * 1j,
            -0.990501697296642 + 0.183694849224890 * 1j,
            1.13549289576738 - 0.552382221616343 * 1j,
            -0.378365978640197 - 0.889536536650390 * 1j,
            2.26109130412416 - 0.989143898037953 * 1j,
            0.794230483767640 - 0.595755572601433 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767641 + 0.595755572601429 * 1j,
            2.26109130412415 + 0.989143898037960 * 1j,
            -0.378365978640198 + 0.889536536650384 * 1j,
            1.13549289576738 + 0.552382221616349 * 1j,
        ],
        [
            -0.136214149861948 + 1.07377729071515 * 1j,
            1.28472431753472 + 0.629797821850576 * 1j,
            -0.990501697296642 + 0.183694849224890 * 1j,
            1.13549289576738 - 0.552382221616345 * 1j,
            -0.378365978640197 - 0.889536536650392 * 1j,
            2.26109130412416 - 0.989143898037953 * 1j,
            0.794230483767641 - 0.595755572601429 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601427 * 1j,
            2.26109130412415 + 0.989143898037961 * 1j,
            -0.378365978640198 + 0.889536536650384 * 1j,
        ],
        [
            2.48622500160235 + 0.775783252972922 * 1j,
            -0.136214149861947 + 1.07377729071516 * 1j,
            1.28472431753472 + 0.629797821850573 * 1j,
            -0.990501697296642 + 0.183694849224896 * 1j,
            1.13549289576738 - 0.552382221616346 * 1j,
            -0.378365978640197 - 0.889536536650388 * 1j,
            2.26109130412415 - 0.989143898037960 * 1j,
            0.794230483767640 - 0.595755572601427 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601429 * 1j,
            2.26109130412416 + 0.989143898037957 * 1j,
        ],
        [
            0.925034243757439 + 0.501055069082895 * 1j,
            2.48622500160235 + 0.775783252972922 * 1j,
            -0.136214149861947 + 1.07377729071516 * 1j,
            1.28472431753472 + 0.629797821850571 * 1j,
            -0.990501697296642 + 0.183694849224894 * 1j,
            1.13549289576738 - 0.552382221616346 * 1j,
            -0.378365978640198 - 0.889536536650384 * 1j,
            2.26109130412415 - 0.989143898037961 * 1j,
            0.794230483767640 - 0.595755572601429 * 1j,
            3.63095734448019 + 0 * 1j,
            0.794230483767640 + 0.595755572601430 * 1j,
        ],
        [
            2.96213213022416 - 0.365264316268174 * 1j,
            0.925034243757439 + 0.501055069082895 * 1j,
            2.48622500160235 + 0.775783252972922 * 1j,
            -0.136214149861947 + 1.07377729071516 * 1j,
            1.28472431753472 + 0.629797821850573 * 1j,
            -0.990501697296642 + 0.183694849224894 * 1j,
            1.13549289576738 - 0.552382221616349 * 1j,
            -0.378365978640198 - 0.889536536650384 * 1j,
            2.26109130412416 - 0.989143898037957 * 1j,
            0.794230483767640 - 0.595755572601430 * 1j,
            3.63095734448019 + 0 * 1j,
        ],
    ]
)


covmat_beamforming = np.array(
    [
        [
            2.86435060461735 + 0.00000000000000 * 1j,
            0.811085737295669 + 1.30227444234303 * 1j,
            0.504301040881477 - 1.00998726806392 * 1j,
            2.72241657929298 - 0.293426536427853 * 1j,
            1.09558286982305 + 1.38724422911377 * 1j,
            0.286520259490070 - 0.792684934007848 * 1j,
            2.59161897333798 - 0.571047494844847 * 1j,
            1.42573311924613 + 1.43217324415322 * 1j,
            0.118079636383169 - 0.521144536970471 * 1j,
            2.43231179623868 - 0.825198584873097 * 1j,
        ],
        [
            0.811085737295669 - 1.30227444234303 * 1j,
            1.84755785331360 + 0.00000000000000 * 1j,
            0.178505290257218 + 0.275885649529008 * 1j,
            0.590249850740701 - 1.26238094293594 * 1j,
            1.79764115658081 - 0.224283298581727 * 1j,
            0.350370057845123 + 0.409182384664349 * 1j,
            0.400773288203037 - 1.15485009350202 * 1j,
            1.81954310603571 - 0.450433700515389 * 1j,
            0.526337242157251 + 0.520857218534430 * 1j,
            0.238850024243051 - 1.04227619126101 * 1j,
        ],
        [
            0.504301040881477 + 1.00998726806392 * 1j,
            0.178505290257218 - 0.275885649529008 * 1j,
            1.57731393536759 + 0.00000000000000 * 1j,
            0.667853435228749 + 1.05824168244305 * 1j,
            0.0631825165171450 - 0.146604502325945 * 1j,
            1.40141246609957 - 0.172573228634075 * 1j,
            0.836133348163892 + 1.05202595933996 * 1j,
            -0.0222793576021373 + 0.0128971713330377 * 1j,
            1.28709132798692 - 0.305699150588609 * 1j,
            1.01531794499543 + 1.00698197341080 * 1j,
        ],
        [
            2.72241657929298 + 0.293426536427853 * 1j,
            0.590249850740701 + 1.26238094293594 * 1j,
            0.667853435228749 - 1.05824168244305 * 1j,
            2.83089465902566 + 0.00000000000000 * 1j,
            0.869864607055596 + 1.39263044682422 * 1j,
            0.421330219272654 - 0.879917604633588 * 1j,
            2.64391169464408 - 0.294939501634435 * 1j,
            1.17982086503835 + 1.48927734106737 * 1j,
            0.210277325342498 - 0.645457934411830 * 1j,
            2.53414257439438 - 0.573735940299302 * 1j,
        ],
        [
            1.09558286982305 - 1.38724422911377 * 1j,
            1.79764115658081 + 0.224283298581727 * 1j,
            0.0631825165171450 + 0.146604502325945 * 1j,
            0.869864607055596 - 1.39263044682422 * 1j,
            2.00142763771913 + 0.00000000000000 * 1j,
            0.208501874874084 + 0.328808413816868 * 1j,
            0.639122890517293 - 1.32641599742298 * 1j,
            1.98057450088836 - 0.230695099267132 * 1j,
            0.377082982336631 + 0.488883425703061 * 1j,
            0.437323828270626 - 1.24168453560702 * 1j,
        ],
        [
            0.286520259490070 + 0.792684934007848 * 1j,
            0.350370057845123 - 0.409182384664349 * 1j,
            1.40141246609957 + 0.172573228634075 * 1j,
            0.421330219272654 + 0.879917604633588 * 1j,
            0.208501874874084 - 0.328808413816868 * 1j,
            1.48342702293691 + 0.00000000000000 * 1j,
            0.573651709810074 + 0.926403794323357 * 1j,
            0.0891883928322622 - 0.208799328917923 * 1j,
            1.32322181458357 - 0.144880533222894 * 1j,
            0.732208466569336 + 0.931568908687762 * 1j,
        ],
        [
            2.59161897333798 + 0.571047494844847 * 1j,
            0.400773288203037 + 1.15485009350202 * 1j,
            0.836133348163892 - 1.05202595933996 * 1j,
            2.64391169464408 + 0.294939501634435 * 1j,
            0.639122890517293 + 1.32641599742298 * 1j,
            0.573651709810074 - 0.926403794323357 * 1j,
            2.71197504118315 + 0.00000000000000 * 1j,
            0.922746605912398 + 1.47213235151886 * 1j,
            0.334424544527173 - 0.728483476348702 * 1j,
            2.55103473133829 - 0.283499225800758 * 1j,
        ],
        [
            1.42573311924613 - 1.43217324415322 * 1j,
            1.81954310603571 + 0.450433700515389 * 1j,
            -0.0222793576021373 - 0.0128971713330377 * 1j,
            1.17982086503835 - 1.48927734106737 * 1j,
            1.98057450088836 + 0.230695099267132 * 1j,
            0.0891883928322622 + 0.208799328917923 * 1j,
            0.922746605912398 - 1.47213235151886 * 1j,
            2.21104428515168 + 0.00000000000000 * 1j,
            0.237978013333236 + 0.418915096142743 * 1j,
            0.690083397770649 - 1.42565896476598 * 1j,
        ],
        [
            0.118079636383169 + 0.521144536970471 * 1j,
            0.526337242157251 - 0.520857218534430 * 1j,
            1.28709132798692 + 0.305699150588609 * 1j,
            0.210277325342498 + 0.645457934411830 * 1j,
            0.377082982336631 - 0.488883425703061 * 1j,
            1.32322181458357 + 0.144880533222894 * 1j,
            0.334424544527173 + 0.728483476348702 * 1j,
            0.237978013333236 - 0.418915096142743 * 1j,
            1.40306815180544 + 0.00000000000000 * 1j,
            0.476886381373807 + 0.778173010784313 * 1j,
        ],
        [
            2.43231179623868 + 0.825198584873097 * 1j,
            0.238850024243051 + 1.04227619126101 * 1j,
            1.01531794499543 - 1.00698197341080 * 1j,
            2.53414257439438 + 0.573735940299302 * 1j,
            0.437323828270626 + 1.24168453560702 * 1j,
            0.732208466569336 - 0.931568908687762 * 1j,
            2.55103473133829 + 0.283499225800758 * 1j,
            0.690083397770649 + 1.42565896476598 * 1j,
            0.476886381373807 - 0.778173010784313 * 1j,
            2.62424195047423 + 0.00000000000000 * 1j,
        ],
    ]
)


def test_doa_music():
    doa, _, _ = proc.doa_music(covmat_est, 3)

    npt.assert_equal(np.sort(doa), np.array([-12, 0, 85]))


def test_doa_root_music():
    doa = proc.doa_root_music(covmat_est, 3)

    npt.assert_almost_equal(
        np.sort(doa),
        np.array([-1.19999999e01, 1.73229939e-07, 8.49999996e01]),
        decimal=3,
    )


def test_doa_esprit():
    doa = proc.doa_esprit(covmat_est, 3)

    npt.assert_almost_equal(doa, np.array([2.025e-15, -1.200e01, 8.500e01]), decimal=3)


def test_doa_bartlett():
    ps = proc.doa_bartlett(covmat_beamforming)

    npt.assert_almost_equal(
        ps,
        np.array(
            [
                -6.23256798,
                -6.21152132,
                -6.14848339,
                -6.04379417,
                -5.89812566,
                -5.7126165,
                -5.48901805,
                -5.22982064,
                -4.938333,
                -4.61869866,
                -4.27584719,
                -3.91539169,
                -3.5434937,
                -3.16672034,
                -2.79191695,
                -2.42611323,
                -2.07647431,
                -1.75030278,
                -1.45509449,
                -1.19865041,
                -0.98924898,
                -0.83588911,
                -0.74862198,
                -0.7390027,
                -0.82071109,
                -1.01041619,
                -1.32898902,
                -1.80318125,
                -2.46777599,
                -3.36750762,
                -4.55463184,
                -6.06242656,
                -7.77056673,
                -8.96624079,
                -8.31032215,
                -5.99932469,
                -3.37297293,
                -1.00296677,
                1.03312153,
                2.7722075,
                4.26157804,
                5.53958415,
                6.63457666,
                7.56693574,
                8.35108429,
                8.99699588,
                9.51124034,
                9.89768303,
                10.15793317,
                10.29160573,
                10.296435,
                10.16825763,
                9.90086521,
                9.48570946,
                8.91142334,
                8.16309861,
                7.22123667,
                6.0602922,
                4.64687043,
                2.93839889,
                0.88651331,
                -1.53577946,
                -4.20647262,
                -6.46045095,
                -7.05360348,
                -6.08177117,
                -4.78210933,
                -3.73038402,
                -3.00308867,
                -2.54456896,
                -2.28317489,
                -2.16404356,
                -2.16369358,
                -2.29729782,
                -2.61785931,
                -3.2081387,
                -4.16193034,
                -5.50920237,
                -6.87322278,
                -6.79749139,
                -4.45960606,
                -1.42028935,
                1.31542695,
                3.58646272,
                5.43649108,
                6.92752655,
                8.10874093,
                9.01515453,
                9.67054507,
                10.09001143,
                10.28161649,
                10.24719085,
                9.98238659,
                9.47594059,
                8.70790771,
                7.64629392,
                6.2409029,
                4.41203715,
                2.03014181,
                -1.11082848,
                -5.1890561,
                -8.67495369,
                -7.18106239,
                -4.29686858,
                -2.34701828,
                -1.2553487,
                -0.8270559,
                -0.95190169,
                -1.58311371,
                -2.71473825,
                -4.35365914,
                -6.42631133,
                -8.4405,
                -9.10036357,
                -7.94229778,
                -6.25015514,
                -4.84945888,
                -3.91099319,
                -3.42220803,
                -3.3480354,
                -3.66384309,
                -4.35678714,
                -5.41354901,
                -6.78187666,
                -8.26522076,
                -9.34993179,
                -9.38159076,
                -8.40576022,
                -7.08616995,
                -5.88535352,
                -4.96171954,
                -4.34202706,
                -4.01532725,
                -3.96485108,
                -4.17662609,
                -4.63985643,
                -5.34249023,
                -6.25964011,
                -7.32747133,
                -8.39447391,
                -9.17683867,
                -9.3504996,
                -8.84005661,
                -7.90143174,
                -6.84642094,
                -5.86200058,
                -5.02467013,
                -4.35458453,
                -3.84902942,
                -3.49761043,
                -3.28835149,
                -3.20990317,
                -3.25216062,
                -3.40622894,
                -3.6640936,
                -4.01810498,
                -4.46026908,
                -4.98127304,
                -5.56914173,
                -6.20744143,
                -6.87309287,
                -7.53426821,
                -8.14964408,
                -8.67121191,
                -9.05267739,
                -9.26237666,
                -9.29437831,
                -9.17000805,
                -8.92859812,
                -8.61421993,
                -8.2657737,
                -7.91282329,
                -7.57561329,
                -7.2669257,
                -6.99424361,
                -6.76157435,
                -6.57079056,
                -6.42254878,
                -6.31689181,
                -6.25362961,
                -6.23256798,
            ]
        ),
        decimal=1,
    )


def test_doa_capon():
    ps = proc.doa_capon(covmat_beamforming)

    npt.assert_almost_equal(
        ps,
        np.array(
            [
                -10.19742531,
                -10.19693874,
                -10.19546992,
                -10.19299188,
                -10.18946106,
                -10.18481957,
                -10.17899842,
                -10.17192207,
                -10.16351448,
                -10.15370678,
                -10.14244694,
                -10.1297115,
                -10.11551932,
                -10.09994754,
                -10.08314889,
                -10.06536995,
                -10.04696876,
                -10.02842985,
                -10.01037395,
                -9.9935586,
                -9.97886549,
                -9.96726956,
                -9.95978522,
                -9.95738627,
                -9.96089788,
                -9.97086308,
                -9.98739026,
                -10.00999275,
                -10.03743528,
                -10.06760299,
                -10.09740612,
                -10.12272794,
                -10.13841462,
                -10.1382966,
                -10.11522288,
                -10.06108341,
                -9.96679091,
                -9.82219054,
                -9.61585988,
                -9.3347506,
                -8.96359855,
                -8.48398166,
                -7.8728113,
                -7.09985713,
                -6.12351664,
                -4.88318275,
                -3.2845658,
                -1.16970761,
                1.74263234,
                5.86058636,
                9.4081819,
                5.94129244,
                1.67756316,
                -1.36463263,
                -3.58585883,
                -5.2706823,
                -6.57774383,
                -7.60068691,
                -8.39908451,
                -9.0136166,
                -9.4740094,
                -9.80348979,
                -10.02144055,
                -10.14505308,
                -10.19037135,
                -10.17293022,
                -10.1080997,
                -10.01120144,
                -9.89743562,
                -9.78162217,
                -9.67771367,
                -9.59799764,
                -9.55192526,
                -9.54463575,
                -9.57547346,
                -9.63698113,
                -9.714805,
                -9.78860948,
                -9.83365423,
                -9.82241592,
                -9.72566034,
                -9.51256621,
                -9.14965531,
                -8.59822302,
                -7.80954469,
                -6.71604395,
                -5.21385966,
                -3.12463787,
                -0.1025276,
                4.5508309,
                9.39286197,
                4.57377175,
                -0.12463796,
                -3.18220375,
                -5.2995547,
                -6.82388039,
                -7.93380716,
                -8.73328673,
                -9.29027275,
                -9.65449183,
                -9.866543,
                -9.96281399,
                -9.9778528,
                -9.94470631,
                -9.89344868,
                -9.84843444,
                -9.82544391,
                -9.83023128,
                -9.85946354,
                -9.90381122,
                -9.95193034,
                -9.99395048,
                -10.02367518,
                -10.03937495,
                -10.0434269,
                -10.04114627,
                -10.03914544,
                -10.04356749,
                -10.05857215,
                -10.08542319,
                -10.12237228,
                -10.16528868,
                -10.20876285,
                -10.24732307,
                -10.27646247,
                -10.29330959,
                -10.29690601,
                -10.28813664,
                -10.2693926,
                -10.24405512,
                -10.21589075,
                -10.18845086,
                -10.16456725,
                -10.14602053,
                -10.13342533,
                -10.1263301,
                -10.12348452,
                -10.12319853,
                -10.12371166,
                -10.12350661,
                -10.12152671,
                -10.11728368,
                -10.11086237,
                -10.10284206,
                -10.09416011,
                -10.08594498,
                -10.0793446,
                -10.07537244,
                -10.07478843,
                -10.07802522,
                -10.08516291,
                -10.09594827,
                -10.10984911,
                -10.12613089,
                -10.14394252,
                -10.16239957,
                -10.18065632,
                -10.19796147,
                -10.21369574,
                -10.22739196,
                -10.23874005,
                -10.24758008,
                -10.25388681,
                -10.25774893,
                -10.2593457,
                -10.25892331,
                -10.25677235,
                -10.25320776,
                -10.24855169,
                -10.2431198,
                -10.23721073,
                -10.23109877,
                -10.2250293,
                -10.21921649,
                -10.21384286,
                -10.20906021,
                -10.20499143,
                -10.20173268,
                -10.19935578,
                -10.19791031,
                -10.19742531,
            ]
        ),
        decimal=1,
    )
